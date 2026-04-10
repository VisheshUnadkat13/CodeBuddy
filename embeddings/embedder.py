# from langchain_ollama import OllamaEmbeddings

# def get_embedding_model():

#     embeddings = OllamaEmbeddings(
#         model="nomic-embed-text"
#     )

#     return embeddings


from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():

    embedding= HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding