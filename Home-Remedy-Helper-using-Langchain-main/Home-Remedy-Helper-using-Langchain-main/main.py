import streamlit as st
from langchain_helper import create_vector_db,qa_chain
st.title("Home Remedy Helper")
button = st.button("Build Repository")
if button:
    pass

question = st.text_input("Question: ")

if question:
    chain = qa_chain()
    reply = chain(question)

    st.header("Answer: ")
    st.write(reply['result'])