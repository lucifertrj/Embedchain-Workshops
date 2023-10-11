# Step-1: Import the required libraries
import streamlit as st
from embedchain import App
from api import getKey
import os
import pandas as pd
# Setup OpenAi api key => Refer documentation and use Open Source App

api_key = getKey()
os.environ['OPENAI_API_KEY'] = api_key
app = App() #First line of Embedchain -> LLM Model

st.title("Heath Assistant Bot")

#In general, we need only 3 line to build a ChatBot-> Embedchain

choice = st.sidebar.selectbox("Pick your choice",("Keto","Vegan"))
st.header(choice)

#Based on the user choice, we are reading the data
if choice == 'Keto':
    file_path = "./Data/keto.csv"
    data = pd.read_csv(file_path)
elif choice == 'Vegan':
    file_path = "./Data/vegan.csv"
    data = pd.read_csv(file_path)

#Display
st.sidebar.dataframe(data.head(10))
#Need to Add the data to App=> LLM
app.add(file_path,data_type="csv") #second line of Embedchain
# Prompt and Query => Response
prompt = st.text_input("Enter your query")
if prompt:
    with st.spinner("Generating..."):
        #third line of Embedchain
        response = app.query(prompt)
        st.write(response)
