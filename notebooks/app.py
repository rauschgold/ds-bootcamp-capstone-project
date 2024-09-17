import streamlit as st
import pickle
import numpy as np
import base64
from best_model import model_wrapper


# Loading trained ML model

with open('best_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Main function of the app
def predict_project_cost(department, year_duration):
    # Define and prepare input data
    input_data = np.array([[department, year_duration]])
    
    # Prediction from model
    prediction = model.predict(input_data)
    
    return prediction

# Streamlit App

# Funktion zum Laden des Hintergrundbildes in Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded_image}"

def main():
    # Hintergrundbild als Base64 einfügen
    bg_image = get_base64_image("../images/Screenshot 2024-09-13 103713.png")
    
    # CSS mit Base64-Bild und Schriftarten
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url({bg_image});
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
    }}
    
     @font-face {{
        font-family: 'Kollektif';
        src: url('fonts/Kollektif.ttf') format('truetype');
    }}

       .body-font {{
        font-family: 'Kollektif';
        font-size: 18px;
        color: black;
    }}

    .centered {{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 10vh;
        margin-top: 10hv;
    }}

    </style>
    """, unsafe_allow_html=True)

    # Subheader with explaination
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.markdown('<p class="body-font"> Select department and enter project length to get a prediction for costs.</p>', unsafe_allow_html=True)

    # Streamlit Inputs
    input_abteilung = st.selectbox("Choose department", ["CO", "CPS", "DBT", "DCMS", "DEFRA", "DEFRA & DFT", "DESNZ", "DFE", "DFID", "DFT", "DHSC", "DLUHC", "DSIT", "DWP", "FCDO", "HMLR", "HMRC", "HMT", "HO", "MOD", "MOJ", "NCA", "NS&I", "ONS", "VOA"])
    input_jahre = st.number_input("Input project length (in years)", min_value=1, step=1)

    # Prediction
    if st.button("Compute prediction"):
        predicted_cost = model_wrapper.predict(input_department, input_year)
        st.write(f"The predicted costs for the project are: {predicted_cost} B £")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
