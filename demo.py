# Best practices you need to follow

# Step-1: Create virtual environment - virtualenv env
# Step-2: Activate: source env/bin/activate
# Step-3: Install modules: pip install embedchain streamlit

# Start with the live demo
import streamlit as st

#Widgets
#1. Title
st.title("Health Assistant Bot")
#2. Heading
st.header("IIT Ropar Workshop")
st.sidebar.header("Workshop by Tarun Jain")

#3. Normal paragraph or Text
st.write("Build a ChatBot like ChatGPT on own data")
#4. Markdown Syntax- Very Important when you are working with Streamlit
st.markdown("# h1")
st.markdown("## h2")
st.markdown("### h3")
st.markdown("#### h4")
st.markdown("##### h5")
st.markdown("###### h6")
st.markdown("[Embedchain Repo](https://github.com/embedchain/embedchain/)")
#5. User Input

username = st.text_input("Enter your name")
if username:
    st.write(username)
bio = st.text_area("Enter your bio")
#6. Button/ Selectbox/Radiobutton or Checkbox

valid = st.button("Click me") #boolean
if valid:
    st.write("Button pressed")

choice = st.selectbox("Fav CWC2023 team",("India","Aus","Eng","NZ"))

#7. File Upload 

uploaded_files = st.file_uploader("Upload your Image")

#streamlit run demo.py
