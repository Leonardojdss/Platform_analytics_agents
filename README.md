# Agentes Analíticos 

Este projeto é uma solução completa que integra agentes especialistas capazes de realizar tarefas de análise de dados. Os agentes deste projeto são capazes de traduzir uma simples pergunta em linguagem natural em query SQL e analisar esses dados para responder à pergunta realizada pelo usuário, além de analisar os dados de forma a trazer insights e recomendações importantes para o usuário. Esse projeto tem como objetivo demonstrar de forma simples o poder do uso dos agentes para conversão de valor da IA generativa.

## Tecnologias Utilizadas

- **CrewAI**: Framework utilizado para criar e gerenciar os agentes responsáveis pela análise de dados e recomendações.
- **Langchain**: Framework utilizado para criar o agente responsável por se conectar ao banco de dados SQL e converter uma pergunta em linguagem natural em uma query.
- **Streamlit**: Framework utilizado para criar a interface web interativa.
- **Azure OpenAI**: Foram utilizados os modelos GPT-4o e GPT-4o-mini para os agentes.

## Agentes

### Agente CrewAI
**Descrição**: Este agente utiliza o framework CrewAI para realizar análises de dados e fornecer recomendações.
**Uso**: O agente CrewAI é responsável por processar o resultado das consultas e fornecer insights detalhados com base nos dados da consulta.

### Agente Langchain
**Descrição**: Este agente utiliza o framework Langchain para se conectar ao banco de dados SQL e converter perguntas em linguagem natural em queries SQL.
**Uso**: O agente Langchain é responsável por traduzir perguntas do usuário em queries SQL, executar essas queries no banco de dados e retornar os resultados para análise.

## Configuração do Ambiente

### Iniciar localmente sem Docker

1. Clone o repositório:
    ```sh
     git clone https://github.com/Leonardojdss/Platform_analytics_agents.git
     cd Platform_analytics_agents
2. Criar ou atualizar o arquivo .env com as variáveis de ambiente necessárias (navegar até a seção Variáveis de Ambiente)
3. Criar um ambiente virtual com virtualenv:
    ```sh
     virtualenv env
     source env/bin/activate
     pip install -r requirements.txt
4. Iniciar o projeto
     ```sh
     streamlit run src/app/main.py

### Iniciar localmente com Docker

1. Clone o repositório:
    ```sh
     git clone https://github.com/Leonardojdss/Platform_analytics_agents.git
     cd Platform_analytics_agents
2. Criar ou atualizar o arquivo .env com as variáveis de ambiente necessárias (navegar até a seção Variáveis de Ambiente)
3. Criar build da imagem Docker
     ```sh
     docker build -t Platform_analytics_agents .
4. Iniciar o container com a imagem criada
     ```sh
     docker run -d -p 8500:8500 Platform_analytics_agents

### Variáveis de Ambiente

As variáveis de ambiente necessárias precisam ser definidas no arquivo `.env`:

```properties
OPENAI_API_TYPE="azure"
OPENAI_API_VERSION="2024-02-01"
AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY"
AZURE_OPENAI_MODEL="gpt-4o"
DB_DRIVERNAME="mssql+pyodbc"
DB_USERNAME="YOUR_DB_USERNAME"
DB_PASSWORD="YOUR_DB_PASSWORD"
DB_HOST="YOUR_DB_HOST"
DB_PORT="1433"
DB_DATABASE="YOUR_DB_DATABASE"
DB_QUERY_DRIVER="ODBC Driver 18 for SQL Server"
AZURE_API_KEY="YOUR_AZURE_API_KEY"
AZURE_API_BASE="YOUR_AZURE_API_BASE"
AZURE_API_VERSION="2024-02-01"
```

## Demonstracao de uso da solução

1. Realize uma pergunta aos seus dados

![alt text](image-1.png)

2. Resultado da sua perguntas com insights e recomendações

![alt text](image-2.png)