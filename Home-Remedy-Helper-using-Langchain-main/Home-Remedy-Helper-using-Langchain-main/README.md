# Home-Remedy-Helper-using-Langchain

This is a Streamlit web application designed to assist users with home remedies. It provides a simple interface for asking questions about health issues and receiving relevant answers based on a predefined dataset.

## Usage

To use the application, follow these steps:

1. **Run the Application**: Execute the script using Streamlit (`streamlit run <script_name>`).
2. **Input Question**: Enter your health-related question in the provided text input field.
3. **View Answer**: After submitting your question, the application will display the corresponding answer based on the dataset.

 You need to provide a CSV file containing the dataset of home remedies. https://www.kaggle.com/datasets/shivanshmittal22/home-remedies
 Use only 'Health issue' and 'Home remedy' columns.

## Functionality
The application utilizes the following components:

- Question-Answer Chain: Implements a question-answer mechanism based on a predefined dataset.
- Vector Database Creation: Builds a vector database for efficient retrieval of relevant information.
- Streamlit Interface: Provides a user-friendly interface for interaction.
