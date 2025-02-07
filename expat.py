import streamlit as st 
import pandas as pd


st.markdown("<h1 style='text-align: center; color: black;'>MY DATA APP</h1>", unsafe_allow_html=True)
#code qui permet d'utiliser du contenues html ou du code simple
st.markdown("""
This app allows you to download scraped data on motocycles from expat-dakar 
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Expat-Dakar](https://www.expat-dakar.com/).
""")


# Fonction de loading des données
def load_(dataframe, title, key) : #load recoit les dataframe, les titres au niveau des boutons et une clé à chzaque fois qu'on crée un bouton #(chemin du dataframe 
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True) #pour mettre du html il, faut mettre à true et false pour mettre du code simple

    if st.button(title,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe) #affiche le dataframe

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)

          
# Charger les données 
load_(pd.read_csv('WebScraper/moto_data_scrape.csv'), 'MOTOS', '1')
load_(pd.read_csv('WebScraper/voiture_data_scrape.csv'), 'VOITURES', '2')
load_(pd.read_csv('WebScraper/pieces_data_scrape.csv'), 'EQUIPEMENTS-PIECES', '3')




 


