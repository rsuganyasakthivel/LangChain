# Web Text QA Tool using Langchain

Web Text QA Tool is a simple question-answering application built using LangChain and Streamlit. This application leverages GooglePalm LLM and HuggingFaceInstructEmbeddings for enhanced performance.

## Features
- **Web URL Integration**: Load web URLs into the application for question answering.
- **Question Input**: Users can type their questions into the interface.
- **Answer Retrieval**: Utilizing LangChain and embeddings, the application attempts to find answers within the provided URLs.
- **Error Handling**: If the answer is found, it displays the answer. If not, it returns 'No answer found'.

## To run the Streamlit app:
- streamlit run main.py
- Note: Create a `.env` file in your project's root directory with API keys in `KEY=VALUE` format.
## Technologies Used
- LangChain
- Streamlit
- GooglePalm
- HuggingFaceInstructEmbeddings.
## Sample Result
![Web Text QA](https://github.com/rsuganyasakthivel/Web-Text-QA-Tool-using-Langchain/blob/main/Sample%20Result.PNG?raw=true)
