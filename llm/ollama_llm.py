# from langchain_community.llms import Ollama

# def load_llm():

#     llm = Ollama(
#         model="llama3.1:8b"
#     )

#     return llm

from langchain_ollama import OllamaLLM

def load_llm():

    llm = OllamaLLM(
        model="llama3.1:8b"
    )

    return llm