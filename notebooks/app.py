import streamlit as st
import pickle
import numpy as np
import base64
from model import get_model

model_wrapper = get_model()


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
    st.markdown('<p class="body-font"> Add your project description, select department and enter project length to get a prediction for costs.</p>', unsafe_allow_html=True)

    # CSS zur Anpassung der Schriftfarbe für Texte außerhalb der Eingabefelder
    st.markdown("""
        <style>
        .stApp div[data-testid="stText"], .stApp div[data-testid="stMarkdownContainer"] {
            color: black !important;
        }
        </style>
        """, unsafe_allow_html=True)

    # Streamlit Inputs
    input_topic = st.text_area("Project Description", placeholder="Add project description")
    input_department = st.selectbox("Choose department", ["CO: Cabinet Office", "CPS: Crown Prosecution Service", "DBT: Department for Business and Trade", "DCMS: Department for Culture, Media and Sport", "DEFRA: Department for Environment, Food and Rural Affairs", "DEFRA & DFT: Department for Environment, Food and Rural Affairs & Department for Transport", "DESNZ: Department for Energy Security and Net Zero", "DFE: Department for Education", "DFID: Department for International Development", "DFT: Department for Transport", "DHSC: Department of Health and Social Care", "DLUHC: Department for Levelling Up, Housing and Communities", "DSIT: Department for Science, Innovation and Technology", "DWP: Department for Work and Pensions", "FCDO: Foreign, Commonwealth & Development Office", "HMLR: Her Majesty's Land Registry", "HMRC: Her Majesty's Revenue and Customs", "HMT: Her Majesty's Treasury", "HO: Home Office", "MOD: Ministry of Defense", "MOJ: Ministry of Justice", "NCA: National Crime Agency", "NS&I: National Savings and Investments", "ONS: Office for National Statistics", "VOA: Valuation Office Agency"])
    input_year = st.number_input("Input project length (in years)", placeholder="Input project length (in years)", min_value=1, step=1)

    st.markdown("""
    <style>
    /* Button-Schriftfarbe auf Grau setzen */
    .stButton>button {
        color: grey !important;
        background-color: #ffed00;  /* Optional: Hintergrundfarbe des Buttons anpassen */
        border: 2px solid black;    /* Optional: Rahmenfarbe des Buttons anpassen */
    }
    </style>
    """, unsafe_allow_html=True)



    # Prediction
    if st.button("Compute prediction"):
        #predicted_cost = model_wrapper.predict(input_department, input_year)
        st.write(f"The predicted costs for the project are: 32 M £")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
