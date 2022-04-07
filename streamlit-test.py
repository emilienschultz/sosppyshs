import streamlit as st
import pandas as pd


st.title("Analyse des flux de travail de l'enquêtre SOSP")

var = ["logiciel_production_donnees","outils_nettoyage","Outils_analyses","Outils_visualisation"]

@st.cache
def load_data():
    data = pd.read_csv("data/SOSP_Export_base de données diffusable.csv")


    #Regrouper toutes les informations dans un seul champ
    data["outils"] = data.apply(lambda x : "|||".join([x[i] for i in var if pd.notnull(x[i])]),axis=1)
    return data

data_load_state = st.text("Chargement des données...")
data = load_data()
data_load_state.markdown("**Données chargées**")

st.text_input("Mot-clé à rechercher", key="motcle") 
v = st.checkbox('Respecter la casse')

if v:
    f = data["outils"].str.lower().str.contains(st.session_state.motcle)
else:
    f = data["outils"].str.contains(st.session_state.motcle)

for i,j in data[f].iterrows():
    st.write(j[var])