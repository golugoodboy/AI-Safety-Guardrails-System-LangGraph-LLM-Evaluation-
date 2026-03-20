def check_confidence(similarity_score):
    if similarity_score < 0.75:
        return "High"
    elif similarity_score < 0.5:
        return "Medium"
    else:
        return "Low"