import streamlit as st
import gensim
from gensim import corpora
from gensim.models import LdaModel, Phrases
from gensim.corpora.dictionary import Dictionary
import nltk
from nltk.stem import WordNetLemmatizer
import string
import pickle

# Load the LDA model
lda_model = LdaModel.load('../models/lda_model.model')

# Load the dictionary
dictionary = Dictionary.load('../models/dictionary.gensim')

# Load the bigram and trigram models
bigram_mod = Phrases.load('../models/bigram_mod.model')
trigram_mod = Phrases.load('../models/trigram_mod.model')

# Load custom stop words
with open('../models/stop_words.pkl', 'rb') as f:
    stop_words = pickle.load(f)

# Ensure necessary NLTK resources are available
nltk.download('punkt')
nltk.download('wordnet')

def clean_text(text):
    replacements = {
        'Âs': ' ',
        '\xa0': ' ',
        '\n': ' ',
        '\r': ' ',
        '\x96': ' ',
        '\t': ' ',
        "\'s": ' ',
        "'s": ' ',
        '\x92': ' ',
        '\x95': ' ',
        '\x93': ' ',
        '\x94': ' ',
        '\x91': ' ',
        "â": ' '
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

lemmatizer = WordNetLemmatizer()

def tokenize(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize and lowercase
    tokens = nltk.word_tokenize(text.lower())
    # Remove stop words, non-alphabetic tokens, and lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalpha() and word not in stop_words]
    return tokens

def make_bigrams(texts):
    return [bigram_mod[doc] for doc in texts]

def make_trigrams(texts):
    return [trigram_mod[bigram_mod[doc]] for doc in texts]

# Set up the Streamlit app
st.title('Project Topic Classifier')

st.write('Enter the project description below to classify its topic.')

# Text input
user_input = st.text_area('Project Description', height=200)

# Button to trigger prediction
if st.button('Classify Topic'):
    if user_input.strip() == '':
        st.write('Please enter a project description.')
    else:
        # Preprocess the user input
        cleaned_input = clean_text(user_input)
        tokenized_input = tokenize(cleaned_input)
        processed_input = make_trigrams([tokenized_input])

        # Convert to BoW format
        input_bow = dictionary.doc2bow(processed_input[0])

        # Get the topic distribution
        input_topics = lda_model.get_document_topics(input_bow, minimum_probability=0)

        # Extract the dominant topic
        sorted_topics = sorted(input_topics, key=lambda x: x[1], reverse=True)
        dominant_topic_num, dominant_topic_prob = sorted_topics[0]
        dominant_topic_keywords = lda_model.show_topic(dominant_topic_num)
        dominant_topic_keywords = ", ".join([word for word, prob in dominant_topic_keywords])

        # Output the results
        st.write(f"**Dominant Topic:** {dominant_topic_num}")
        st.write(f"**Probability:** {dominant_topic_prob:.4f}")
        st.write(f"**Keywords:** {dominant_topic_keywords}")

        ## Optionally, map the topic number to its label if you have a topic_labels dictionary
        # topic_labels = {
        #     0: 'Machine Learning Applications',
        #     1: 'Climate Change Impact',
        #     2: 'Renewable Energy Solutions',
        #     # ... continue for all topics
        # }

        # topic_label = topic_labels.get(dominant_topic_num, "Unknown Topic")
        # st.write(f"**Topic Label:** {topic_label}")