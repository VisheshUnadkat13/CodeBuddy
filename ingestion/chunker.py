from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_code(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = []

    for doc in docs:

        split = splitter.split_text(doc["content"])

        for s in split:

            chunks.append({
                "text":s,
                "source":doc["source"]
            })

    return chunks