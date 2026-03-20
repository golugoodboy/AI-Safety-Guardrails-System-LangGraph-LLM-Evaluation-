from retrieval.retriever import get_retriver
from llm.generator import generate_answers
from safety.hallucination import check_hallucination
from safety.confidence import check_confidence
from llm.verifier import verify_answer
from utils.embeddings import get_embedding
from utils.logger import log_result


document = [
    "Paris is the capital of France.",
    "Berlin is the capital of Germany.",
    "Tokyo is the capital of Japan."
]

retriever = get_retriver(document)

def run_pipeline(query):
    #retrieval
    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])

    #generate answer
    answer = generate_answers(query, context)

    #embeddings
    answer_embedding = get_embedding(answer)
    context_embeddings = [get_embedding(doc.page_content) for doc in docs]

    #hallucination check
    is_hallucinated, similarity = check_hallucination(answer_embedding, context_embeddings)

    #confidence check
    confidence = check_confidence(similarity)

    #verifier
    is_verified = verify_answer(answer, context, query)

    #final decision logic
    if is_hallucinated or is_verified == "False":
        status = "❌ Unsafe / Hallucinated"
    elif confidence == "Medium":
        status = "⚠️ Low Confidence"
    else: 
        status = "✅ Safe"

    log_result({
    "query": query,
    "answer": answer,
    "confidence": confidence,
    "similarity_score": float(similarity),
    "verification": is_verified,
    "status": status
})
    return {
        "query": query,
        "answer": answer,
        "confidence": confidence,
        "similarity_score": similarity,
        "verification": is_verified,
        "status": status
    }

if __name__ == "__main__":
    result = run_pipeline("What is the capital of Germany?")
    print(result)

    for key, value in result.items():
        print(f"{key} : {value}")


