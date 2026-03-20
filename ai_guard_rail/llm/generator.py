from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2-7B-Instruct",
    task="text-generation",
    max_new_tokens = 300,
    do_sample = False,
    temperature=0.1,
    repetition_penalty=1.1,
)

model = ChatHuggingFace(llm = llm)

def generate_answers(query, context):
    prompt = f"""
    Answer the question based ONLY on the context.

    Context:
    {context}

    Question:
    {query}
    """

    response = model.invoke([{"role" : "user", "content" : prompt}]).content
    
    return response

