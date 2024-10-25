import streamlit as st
from sqlalchemy import create_engine  
from sqlalchemy.engine.url import URL  
from langchain_community.utilities import SQLDatabase  
import os  
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI 
#from langchain.agents import AgentExecutor  
from langchain.agents.agent_types import AgentType  
from langchain_community.agent_toolkits.sql.base import create_sql_agent  
from crewai import LLM, Agent, Task, Crew
import warnings

load_dotenv()

# Desativar warnings
warnings.filterwarnings("ignore")

def load_environment_variables():
    os.environ["OPENAI_API_TYPE"] = "azure"  
    os.environ["OPENAI_API_VERSION"] = "2023-05-15"
    os.environ["AZURE_ENDPOINT"] = "https://northcentralus.api.cognitive.microsoft.com/openai"  
    os.environ["OPENAI_API_KEY"] = "231bbdf2f44742cb92410beb990486ce"

def get_database_connection():
    db_config = {  
        'drivername': 'mssql+pyodbc',  
        'username': "admindba",  
        'password': "L989644@thelast",  
        'host': "tcp:appgeninsights.database.windows.net,1433",  
        'port': 1433,  
        'database': "db_app",  
        'query': {'driver': 'ODBC Driver 18 for SQL Server'}  
    }  
    db_url = URL.create(**db_config)  
    return SQLDatabase.from_uri(db_url)

def create_langchain_agent(db, llm):
    from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit  
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)  
    return create_sql_agent(  
        llm=llm,  
        toolkit=toolkit,  
        verbose=True,  
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  
    )

def execute_query(agent_executor, query):
    try:  
        return agent_executor.invoke(query)  
    except Exception as e:  
        print(f"Ocorreu um erro: {e}")
        return None

def create_crew_agents(llm_openai_gpt4o):
    cientista_de_dados = Agent(
        role="cientista de dados",
        goal="Realizar uma análise dos dados fornecido pelo agente do langchain",
        backstory=(
            "Você é um Analista de Dados experiente, especializado em coletar, \
            processar e analisar grandes volumes de dados para extrair insights\
            valiosos. Sua comunicação é clara, objetiva e baseada em fatos.\
            Você utiliza ferramentas e técnicas avançadas de análise de dados para\
            apoiar a tomada de decisões estratégicas. "
        ),
        allow_delegation=False,
        verbose=True,
        llm=llm_openai_gpt4o)

    analista_de_geracao_recomendacoes = Agent(
        role="Analista de Geração de Recomendações",
        goal="Fornecer recomendações com base em análises de dados provenientes do setor de telecomunicações, otimizando estratégias de venda, atendimento ao cliente e melhoria de infraestrutura de rede.",
        backstory=(
            "Este agente é responsável por transformar dados complexos em recomendações acionáveis, "
            "focando no aumento da eficiência dos serviços de telecomunicações e na melhoria da experiência dos clientes. "
            "Ele colabora diretamente com cientistas de dados para interpretar modelos preditivos e fornecer recomendações estratégicas."
        ),
        allow_delegation=False,
        verbose=True,
        llm=llm_openai_gpt4o)

    # revisao_de_texto = Agent(
    #     role="Analista de Geração de Texto em Markdown",
    #     goal="Transformar as recomendações e análises técnicas em relatórios claros e organizados, formatados em Markdown para fácil compartilhamento.",
    #     backstory=(
    #         "Este agente é especializado em redigir e revisar documentos técnicos e relatórios estratégicos "
    #         "em linguagem Markdown. Ele é responsável por traduzir dados técnicos e recomendações em um formato acessível, "
    #         "garantindo que as informações sejam bem estruturadas e fáceis de entender para tomadores de decisão."
    #     ),
    #     allow_delegation=False,
    #     verbose=True,
    #     llm=llm_openai_gpt4o
    # )

    return [cientista_de_dados, analista_de_geracao_recomendacoes]

def create_crew_tasks(output, agents):
    tarefa_cientista_de_dados = Task(
        description=(f"1. Analisar o retorno da query do agente da langChain, Realizar uma análise como um cientista de dados,\
                     segue retorno\n: {output}"),
        expected_output=("Análise detalhada do retorno da query do agente da langChain"),
        agent=agents[0]
    )

    tarefa_de_recomendacoes = Task(
        description=(
            "Receber a análise prescritiva ou descritiva do cientista de dados sobre os dados de telecomunicações analisados"
        ),
        expected_output=(
            "Relatório contendo recomendações estratégicas sobre os dados analisados, Texto precisa estar formatado com markdown"
        ),
        agent=agents[1]
    )

    # tarefa_revisao_de_texto = Task(
    #     description=(
    #         "Receber as recomendações geradas pelo Analista de Geração de Recomendações e transformá-las em um relatório em markdown."
    #         "estruturado em Markdown, garantindo clareza e precisão nas informações apresentadas."
    #     ),
    #     expected_output=(
    #         "Documento em Markdown contendo as recomendações bem organizadas, com seções claras e objetivas, "
    #         "de forma sucinta e objetiva."
    #     ),
    #     agent=agents[2]
    # )

    return [tarefa_cientista_de_dados, tarefa_de_recomendacoes]

def main():
    load_environment_variables()
    db = get_database_connection()
    llm_azure_langchain = AzureChatOpenAI(deployment_name="gpt-4o-max", temperature=0)
    agent_executor = create_langchain_agent(db, llm_azure_langchain)
    
    st.title("APP - GenInsight")
    user_input = st.text_input("Digite sua pergunta:")
    
    if user_input:
        output = execute_query(agent_executor, user_input)
        
        if output:
            #st.write("Resposta do agente da LangChain:\n\n", output)
        
            openai_api_key = "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" 
            llm_openai_gpt4o = LLM(model="gpt-4o-mini", 
                                   temperature=0, 
                                   api_key=openai_api_key, 
                                   top_p=1)
            
            agents = create_crew_agents(llm_openai_gpt4o)
            tasks = create_crew_tasks(output, agents)
            
            crew = Crew(agents=agents, tasks=tasks, verbose=True, memory=True)
            result = crew.kickoff()
            print(result)
            
            #revisao_de_texto_output = tasks[2].expected_output
            st.markdown(f"<div style='word-wrap: break-word;'>{result}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
