import json
from main import run_pipeline

def load_data(path = "data.json"):
    with open(path, "r") as f:
        return json.load(f)

def evaluate_hallucination():
    data = load_data()

    correct = 0
    total = len(data)

    for item in data:
        result = run_pipeline(item["query"])

        predicted = "Unsafe" in result["status"]
        actual = item["is_hallucination"]

        if predicted == actual:
            correct += 1

        print("----")
        print("Query:", item["query"])
        print("Expected Hallucination:", actual)
        print("Predicted:", predicted)
        print("Status:", result["status"])

    accuracy = correct / total

    print("\n🎯 Hallucination Detection Accuracy:", accuracy)

    return accuracy

if __name__ == "__main__":
    evaluate_hallucination()