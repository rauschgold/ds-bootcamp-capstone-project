import streamlit as st
import pickle
import numpy as np


# Loading trained ML model

with open('../data/pickle/best_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Main function of the app
def predict_project_cost(department, year_duration):
    # Define and prepare input data
    input_data = np.array([[department, year_duration]])
    
    # Prediction from model
    prediction = model.predict(input_data)
    
    return prediction

# Streamlit App
def main():
     # Global Style Settings
    st.markdown("""
    <style>
                
    /* background */
    body {
        background-image: url('../images/Screenshot 2024-09-13 103713.png?v=1');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    @font-face {
        font-family: 'Espa';
        src: url('fonts/espa.otf') format('opentype');
        font-weight: normal;
        font-style: normal;
    }
    @font-face {
        font-family: 'Kollektif';
        src: url('fonts/Kollektif.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
    }

    /* Font for Title */
    .title-font {
        font-family: 'Espa', sans-serif;
        font-size: 40px;
        color: black;
        font-weight: bold;
    }

    /* Font for Body */
    .body-font {
        font-family: 'Kollektif', sans-serif;
        font-size: 18px;
        color: black;
    }

    /* Style for highlighted blocks */
    .highlight {
        background-color: #ffed00;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="title-font">Public Project Predictor</p>', unsafe_allow_html=True)

    st.markdown('<p class="body-font">Select Department and enter Project Length to get a Predicition for Costs.</p>', unsafe_allow_html=True)

    
    # Input for user
    project_name = st.text_input("Project Name")
    department = st.selectbox("Department", ["CO", "CPS", "DBT", "DCMS", "DEFRA", "DEFRA & DFT", "DESNZ", "DFE", "DFID", "DFT", "DHSC", "DLUHC", "DSIT", "DWP", "FCDO", "HMLR", "HMRC", "HMT", "HO", "MOD", "MOJ", "NCA", "NS&I", "ONS", "VOA"])
    project_length_years = st.number_input("Planned Project Length (in years)", min_value=1, step=1)
    
    if st.button("Prediction"):
        cost = predict_project_cost(department, project_length_years)
        st.success(f"The predicted costs for the project '{project_name}' are: {cost:.2f} B £")

if __name__ == "__main__":
    main()
