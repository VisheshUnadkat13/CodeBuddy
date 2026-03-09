from utils.prompt_templates import BUG_PROMPT

def detect_bugs(query,retriever,llm):

    docs = retriever.invoke(query)

    context = "\n".join([d.page_content for d in docs])

    prompt = BUG_PROMPT.format(context=context)

    response = llm.invoke(prompt)

    return response,docs