from utils.prompt_templates import CHAT_PROMPT
from rag.bug_detector import detect_bugs
from rag.doc_generator import generate_docs
from rag.contributor_guide import guide_contributor

def run_rag(query,mode,retriever,llm):

    if mode=="Bug Detection":

        return detect_bugs(query,retriever,llm)

    elif mode=="Generate Documentation":

        return generate_docs(query,retriever,llm)

    elif mode=="Open Source Contributor":

        return guide_contributor(query,retriever,llm)


    else:

        docs = retriever.invoke(query)

        context = "\n".join([d.page_content for d in docs])

        prompt = CHAT_PROMPT.format(
            context=context,
            query=query
        )

        response = llm.invoke(prompt)

        return response,docs