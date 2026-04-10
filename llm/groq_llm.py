# from langchain_community.llms import Ollama

# def load_llm():

#     llm = Ollama(
#         model="llama3.1:8b"
#     )

#     return llm

from langchain_groq import ChatGroq
import os

def load_llm():
         from dotenv import load_dotenv
         load_dotenv()
    
         api_key=os.getenv("GROQ_API_KEY")
         if not api_key:
            raise ValueError("GROQ_API_KEY not found")
            
        
         llm = ChatGroq(
            api_key=api_key,
            model_name="llama-3.3-70b-versatile"
    )
         return llm