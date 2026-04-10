from utils.prompt_templates import CONTRIBUTOR_PROMPT

def guide_contributor(query, retriever, llm):
    docs = retriever.invoke(query)
    context = "\n".join([d.page_content for d in docs])
    prompt = CONTRIBUTOR_PROMPT.format(context=context, query=query)
    response = llm.invoke(prompt)
    return response, docs
