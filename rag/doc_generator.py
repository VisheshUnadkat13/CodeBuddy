from utils.prompt_templates import DOC_PROMPT

def generate_docs(query,retriever,llm):

    docs = retriever.invoke(query)

    context = "\n".join([d.page_content for d in docs])

    prompt = DOC_PROMPT.format(context=context)

    response = llm.invoke(prompt)

    return response,docs