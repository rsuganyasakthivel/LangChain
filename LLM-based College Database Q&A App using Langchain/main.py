import streamlit as st

from dbchain_fewshort_helper import get_db_chain_with_fewshot

st.title("College Database Q&A")

# Displaying images on the front end
from PIL import Image
image = Image.open('clg_img.png')

st.image(image)

st.write("Greetings!! May I help you? ")
question = st.text_input("Question: ")

if question:
    chain = get_db_chain_with_fewshot()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)