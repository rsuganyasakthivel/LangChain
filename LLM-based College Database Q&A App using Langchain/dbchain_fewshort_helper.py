from langchain.llms import GooglePalm

import os
from dotenv import load_dotenv

load_dotenv()

from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt

from few_shots import few_shots

def get_db_chain_with_fewshot():
    llm = GooglePalm(temperature=0.1)

    db_user = "root"
    db_pwd = "root"
    db_host = "localhost"
    db_name = 'college_db'

    db = SQLDatabase.from_uri(f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}/{db_name}',
                              sample_rows_in_table_info=4)
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    combined_text = [" ".join(dict_item.values()) for dict_item in few_shots]

    vector_database = Chroma.from_texts(combined_text, embeddings, metadatas=few_shots)

    similar_example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vector_database,
        k=2,
    )

    prompt_for_example = PromptTemplate(
    input_variables=['Answer','Question','SQLQuery','SQLResult'],
        template='\nAnswer:{Answer}\n Question:{Question}\n SQLQuery:{SQLQuery}\n SQLResult:{SQLResult}'
    )

    few_shot_prompt_template = FewShotPromptTemplate(
        example_selector=similar_example_selector,
        example_prompt=prompt_for_example,
        prefix=_mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],
    )

    db_chain_with_fewshot = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt_template,use_query_checker=True)

    return db_chain_with_fewshot

if __name__ == '__main__':
    chain = get_db_chain_with_fewshot()
    print(chain.run("Which professor who is not a HOD gets the lowest salary?"))