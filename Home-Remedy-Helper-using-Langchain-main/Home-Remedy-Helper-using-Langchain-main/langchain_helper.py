import os
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

from langchain.llms import GooglePalm
llm = GooglePalm(google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0)

loader = CSVLoader(file_path='Home Remedies_QA.csv',source_column='Health Issue')
data = loader.load()

instructor_embedding = HuggingFaceInstructEmbeddings()

vector_db_file = 'FAISS_index'
def create_vector_db():
    loader = CSVLoader(file_path='Home Remedies_QA.csv', source_column='Health Issue')
    data = loader.load()
    vector_db = FAISS.from_documents(documents=data, embedding=instructor_embedding)
    vector_db.save_local(vector_db_file)

def qa_chain():
    # Load the vector db from the local folder
    vector_db = FAISS.load_local(vector_db_file,instructor_embedding)
    retriever = vector_db.as_retriever()

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain_type_kwargs = {"prompt": PROMPT}

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type='stuff',
                                        retriever=retriever,
                                        input_key='query',
                                        return_source_documents=True,
                                        chain_type_kwargs=chain_type_kwargs)
    return chain

if __name__ == "__main__":
    # create_vector_db()
    chain = qa_chain()
    print(chain("What is the reason for hiccups?"))
    print(chain("What is the home remedy for constipation?"))
    print(chain("What is the home remedy for Dehydration?"))
