from sklearn.metrics.pairwise import cosine_similarity

def check_hallucination(answer_emb, context_embs):
    scores = [cosine_similarity([answer_emb], [ctx_emb])[0][0] for ctx_emb in context_embs]
    max_score = max(scores)

    if max_score < 0.5:  # lowered threshold
        return True, max_score
    
    return False, max_score