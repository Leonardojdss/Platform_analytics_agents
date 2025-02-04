from langchain_openai import AzureChatOpenAI 
import os
from dotenv import load_dotenv

load_dotenv()

class azure_openai:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            deployment_name=os.getenv("AZURE_OPENAI_MODEL"), 
            temperature=0
        )
    
    def get_connection(self):
        return self.llm 