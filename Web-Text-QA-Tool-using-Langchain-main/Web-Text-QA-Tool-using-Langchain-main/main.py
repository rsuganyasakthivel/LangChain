import os
import streamlit as st
import pickle
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import GooglePalm

from dotenv import load_dotenv
load_dotenv()

st.title("Web Text QA Tool")
st.sidebar.title("Data URLs")

urls = []
for i in range(2):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store.pkl"

main_placeholder = st.empty()
llm = GooglePalm(temperature=0, max_tokens=500)

if process_url_clicked:
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Loading Data .....")
    data = loader.load()
    # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=[
            "\n\n",
            "\n",
            " ",
            ".",
            ",",
            "\u200B",  # Zero-width space
            "\uff0c",  # Fullwidth comma
            "\u3001",  # Ideographic comma
            "\uff0e",  # Fullwidth full stop
            "\u3002",  # Ideographic full stop
            "",
        ],
        chunk_size=1000
    )
    docs = text_splitter.split_documents(data)

    # create embeddings and save it to vector database
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")

    vectorstore = FAISS.from_documents(docs, embeddings)

    # Save the FAISS index to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore, f)

query = main_placeholder.text_input("Question: ")

if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQA.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain({"query": query}, return_only_outputs=True)
            if result:
                st.header("Answer")
                st.write(result['result'])
            else:
                st.write("No answer found.")