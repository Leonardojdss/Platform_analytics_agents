from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit  
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.agents.agent_types import AgentType    


def create_langchain_agent_sql(db, llm):
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)  
    return create_sql_agent(  
        llm=llm,  
        toolkit=toolkit,  
        verbose=True,  
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True  
    )