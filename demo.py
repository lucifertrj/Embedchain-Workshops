# Best Practice to install Python libraries/module
#Step 1: Create a Virtual environment: virtualenv tarun
#Step 2: Activate => source tarun/bin/activate
#Step 3: Install libraries => pip install embedchain streamlit

def do_something():
    st.write("Hello, you clicked the button!")
#Demo
# 5-6 different widgets
import streamlit as st
#title
st.title("Health Assistant Bot")
#header
st.header("Embedchain- Build ChatBot like ChatGPT")
#normal text 
st.write("Let's build an Health assistant bot on custom data")
#user input -  name
name = st.text_input("Enter your name")
if name:
    st.write("Greetings "+name)
#user input - user bio
bio = st.text_area("Enter your bio")
# button
btn = st.button("Click here")
if btn:
    st.write("Button clicked")
    #also 
    do_something()

st.markdown("[Embedchain GitHub Repo](https://github.com/embedchain/embedchain/tree/main/embedchain)")
st.markdown("![dog](https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*)")


upload_file = st.file_uploader("Upload your PDF")

# Run our application
# streamlit run demo.py
