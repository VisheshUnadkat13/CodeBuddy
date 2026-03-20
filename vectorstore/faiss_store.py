# from langchain_community.vectorstores import FAISS

# def create_vector_store(chunks, embeddings):

#     texts = [c["text"] for c in chunks]

#     metadata = [{"source":c["source"]} for c in chunks]

#     db = FAISS.from_texts(
#         texts,
#         embeddings,
#         metadatas=metadata
#     )

#     return db

from langchain_community.vectorstores import FAISS

def create_vector_store(chunks, embeddings):

    if len(chunks) == 0:
        raise ValueError("No code chunks found. Repository may be empty.")

    texts = [c["text"] for c in chunks]
    metadata = [{"source": c["source"]} for c in chunks]

    db = FAISS.from_texts(
        texts,
        embeddings,
        metadatas=metadata
    )

    return db