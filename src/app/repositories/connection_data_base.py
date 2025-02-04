from sqlalchemy.engine.url import URL  
from langchain_community.utilities import SQLDatabase 
from dotenv import load_dotenv
import os 

load_dotenv() 

def get_database_connection():
    db_config = {  
        'drivername': os.getenv("DB_DRIVERNAME"),  
        'username': os.getenv("DB_USERNAME"),  
        'password': os.getenv("DB_PASSWORD"),  
        'host': os.getenv("DB_HOST"),  
        'port': int(os.getenv("DB_PORT")),  
        'database': os.getenv("DB_DATABASE"),  
        'query': {'driver': os.getenv("DB_QUERY_DRIVER")}  
    }  
    db_url = URL.create(**db_config)  
    return SQLDatabase.from_uri(db_url)