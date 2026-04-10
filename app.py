import streamlit as st

from ingestion.repo_loader import clone_repo
from ingestion.code_parser import load_code_files
from ingestion.chunker import chunk_code

from embeddings.embedder import get_embedding_model
from vectorstore.faiss_store import create_vector_store
from retriever.retriever import get_retriever

from llm.groq_llm import load_llm
from rag.rag_pipeline import run_rag

st.set_page_config(page_title="CodeBuddy AI")

st.title("CodeBuddy AI")

repo = st.text_input("Enter GitHub Repo URL")

mode = st.selectbox(
    "Select Mode",
    [
        "Chat with Code",
        "Bug Detection",
        "Generate Documentation",
        "Open Source Contributor"
    ]
)

if st.button("Load Repository"):

    path = clone_repo(repo)

    docs = load_code_files(path)

    chunks = chunk_code(docs)

    embeddings = get_embedding_model()

    db = create_vector_store(chunks,embeddings)

    retriever = get_retriever(db)

    llm = load_llm()

    st.session_state.retriever = retriever
    st.session_state.llm = llm

    st.success("Repository Indexed")

query = st.text_input("Ask something about the code")

if st.button("Run"):

    response,docs = run_rag(
        query,
        mode,
        st.session_state.retriever,
        st.session_state.llm
    )

    if hasattr(response, 'content'):
        st.markdown(response.content)
    else:
        st.markdown(response)

    st.subheader("Sources")

    for d in docs:

        st.write(d.metadata)