from llm.generator import model

def verify_answer(answer,context,question):
    prompt = f"""
    You are a verifier.
    Check if the answer is relevant to the question and based on the context.
    
    Context:
    {context}
    
    Question:
    {question}
    
    Answer:
    {answer}
    
    Return True if the answer is relevant and based on the context, False otherwise.
    """
    response = model.invoke([{"role" : "user", "content" : prompt}]).content
    return response

