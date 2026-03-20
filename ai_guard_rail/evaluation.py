import json

def load_logs(file = "logs.jsonl"):
    with open(file, "r") as f:
        return [json.loads(line) for line in f]


def evaluate_logs(logs):
    total = len(logs)

    safe_count = 0
    hallucinated_count = 0
    low_confidence_count = 0

    for log in logs:
        status = log["data"]["status"]

        if "Safe" in status:
            safe_count += 1
        elif "Hallucinated" in status:
            hallucinated_count += 1
        elif "Low Confidence" in status:
            low_confidence_count += 1

    return {
        "total": total,
        "safe": safe_count,
        "hallucinated": hallucinated_count,
        "low_confidence": low_confidence_count
    }

if __name__ == "__main__":
    logs = load_logs()
    evaluation = evaluate_logs(logs)
    print(evaluation)