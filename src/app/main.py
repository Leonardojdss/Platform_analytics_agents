import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
import os  
from dotenv import load_dotenv
import warnings
from app.repositories.connection_data_base import get_database_connection
from app.repositories.connection_azure_openai import azure_openai
from app.agents.agent_langchain import create_langchain_agent_sql
from app.service.execution_langchain import agent_langchain_execute_query
from app.service.execution_crewai import agent_crewai_execute_analysis

load_dotenv()

# Desativar warnings
warnings.filterwarnings("ignore")

def main():

    #dicionarios dos dados
    path = "src/app/dicionarios_dados.txt"
    with open(path, "r") as file:
        dicionario = file.read()
    print(dicionario)

    db = get_database_connection()
    llm_azure_langchain = azure_openai().get_connection()
    agent_executor = create_langchain_agent_sql(db, llm_azure_langchain)
    
    st.title("APP - GenInsight")
    user_input = st.text_input("Digite sua pergunta:")
    user_input_final = dicionario + "n/n/" + user_input

    if user_input:
        output = agent_langchain_execute_query(agent_executor, user_input_final)
        #output = "faturamento de 100.000"

        if output:

            result = agent_crewai_execute_analysis(output)
            print(result)
            
            st.markdown(f"<div style='word-wrap: break-word;'>{result}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
