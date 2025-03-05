import streamlit as st
import numpy as np
import pickle

# Charger le modèle
model = pickle.load(open(r"D:\Streamlit\Streamlit2\str2.py", "rb"))

st.title("Prédiction de possession de compte bancaire")

# Formulaire pour les entrées utilisateur
country = st.selectbox("Pays", options=['Kenya', 'Rwanda', 'Tanzania', 'Uganda'])
location_type = st.selectbox("Type de lieu", options=['Rural', 'Urban'])
cellphone_access = st.selectbox("Accès au téléphone", options=['Yes', 'No'])
household_size = st.number_input("Taille du ménage", min_value=1, max_value=20, value=1)
age_of_respondent = st.number_input("Âge", min_value=18, max_value=100, value=30)

# Bouton de prédiction
if st.button("Prédire"):
    input_data = np.array([[household_size, age_of_respondent]])
    prediction = model.predict(input_data)
    st.success(f"Résultat de la prédiction: {'Possède un compte' if prediction[0] == 1 else 'Ne possède pas de compte'}")