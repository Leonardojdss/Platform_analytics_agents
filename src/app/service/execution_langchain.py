



def agent_langchain_execute_query(agent_executor, query):
    try:  
        return agent_executor.invoke(query)  
    except Exception as e:  
        erro = print(f"Ocorreu um erro: {e}")
        return erro