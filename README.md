<img width="2544" height="874" alt="CodeBuddy WorkFlow" src="https://github.com/user-attachments/assets/803e75aa-e545-4dfc-8014-098dd78b0ba7" />
<img width="1577" height="1040" alt="Screenshot 2026-03-09 212327" src="https://github.com/user-attachments/assets/f1af2c27-7c46-4bb2-ab73-6db1599b5f49" />
<img width="1919" height="1140" alt="Screenshot 2026-03-09 212342" src="https://github.com/user-attachments/assets/17145f05-5390-4bd5-b718-1e4c75228a33" />
<img width="1919" height="1137" alt="Screenshot 2026-03-09 212412" src="https://github.com/user-attachments/assets/3416d0d3-cc58-4cf1-816a-006205dc4792" />
<img width="1919" height="1135" alt="Screenshot 2026-03-09 212428" src="https://github.com/user-attachments/assets/09dbb813-2069-4e1b-be63-8ff502db673b" />
<img width="1919" height="1139" alt="Screenshot 2026-03-09 212627" src="https://github.com/user-attachments/assets/44f776d0-e5c3-4f37-a252-5ba7e38f6008" />

# 🚀 CodeBuddy AI

**CodeBuddy AI** is an intelligent **AI-powered codebase assistant** that allows developers to interact with large code repositories using **natural language queries**.  

It uses **Retrieval-Augmented Generation (RAG)** to analyze source code, retrieve relevant code snippets, and generate contextual responses using a Large Language Model.

The system can help developers **understand unfamiliar codebases, detect bugs, and generate documentation automatically.**

---

# ✨ Features

- 🔍 **Codebase Semantic Search**  
  Query any repository using natural language.

- 🐞 **AI Bug Detection**  
  Identify potential issues in the code.

- 📝 **Automatic Code Documentation**  
  Generate human-readable documentation for code files.

- 🧠 **Context-Aware Code Explanation**  
  Understand large repositories using RAG-based retrieval.

- ⚡ **Fast Similarity Search**  
  Uses FAISS vector database for efficient retrieval.

- 🌐 **Interactive UI**  
  Built with Streamlit for easy interaction.

---

# 🏗 System Architecture

User Query
↓
Streamlit UI
↓
Repository Ingestion
↓
Code Parsing
↓
Code Chunking
↓
Embedding Generation
↓
FAISS Vector Database
↓
Retriever
↓
Llama3 (Ollama LLM)
↓
AI Response


---

# ⚙️ Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## AI / LLM
- LangChain
- Ollama
- Llama3

## Embeddings
- nomic-embed-text

## Vector Database
- FAISS

## Other Tools
- GitPython
- RecursiveCharacterTextSplitter

---

💡 How It Works

User provides a GitHub repository path.
The system loads and parses all code files.
Files are split into smaller semantic chunks.
Each chunk is converted into embeddings.
Embeddings are stored in a FAISS vector database.
When a user asks a question:
Relevant code chunks are retrieved.
Context is passed to the LLM.
Llama3 generates the final answer.

🔮 Future Improvements

AST-based code understanding
AI-generated unit tests
Pull request code review
Multi-repository support
GitHub integration
Agent-based workflows with LangGraph

👨‍💻 Author
Vishesh Unadkat
