#Import the library
import streamlit as st
#Installation: pip install streamlit
#Running Syntax: streamlit run <filename.py>
#Running Example: streamlit run demo.py

#Widget=> Building blocks of Streamlit
#1. Title 
st.title("Embedchain Workshop")
#2. Heading
st.header("IIT Bombay")
#3. Markdown -> Document language that ends with .md file
st.markdown("# Heading1")
st.markdown("## Heading2")
st.markdown("### Heading3")
st.markdown("#### Heading4")
st.markdown("##### Heading5")
st.markdown("###### Heading6")
st.markdown("[Embedchain GitHub Repo](https://github.com/embedchain/embedchain/issues)")

#4. Normal paragraph
st.write("aonwbvsns[pfobfoldcdvonfdvnlmd;   wmm]")

#5. Sidebar
st.sidebar.title("Research Paper Bot")
st.sidebar.markdown("[Source Code](https://github.com/lucifertrj/Embedchain-Workshops/tree/main/ResearchPaperBot)")

#6. User Input

#text input => Small entry box to enter
#text area => Larger entry box to enter
user_input = st.text_area("Enter your Name")
st.write(user_input)

#7. Button
#return in Boolean
btn = st.button("Click here")
if btn:
    st.markdown("Hi, How are you?")
    
# 8. Selectbox
choice = st.selectbox("CWC23",("Ind vs Pak","Eng vs NZ"))
    