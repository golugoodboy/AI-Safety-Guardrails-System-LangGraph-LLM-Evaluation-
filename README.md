# 🛡️ AI Safety & Guardrails System

An advanced AI system designed to improve Large Language Model (LLM) reliability by detecting hallucinations, scoring confidence, and enforcing safety guardrails using a LangGraph-based workflow.

---

## 🚀 Overview

This project builds a **production-style AI safety layer** on top of LLMs. It evaluates generated responses using multiple validation signals and ensures that outputs are reliable, safe, and grounded in context.

---

## 🔥 Key Features

* ✅ Hallucination Detection using embedding similarity
* ✅ Confidence Scoring (High / Medium / Low)
* ✅ Self-Verification using LLM feedback
* ✅ LangGraph-based workflow orchestration
* ✅ Automated Retry Mechanism for unsafe responses
* ✅ Logging system for tracking model behavior
* ✅ Evaluation metrics (accuracy, safety rate, similarity trends)
* ✅ Drift detection (performance monitoring over time)
* ✅ Streamlit dashboard for real-time interaction

---

## 🧠 System Architecture

```
User Query
   ↓
Context Retrieval (FAISS)
   ↓
LLM Response Generation
   ↓
Hallucination Detection (Embeddings)
   ↓
LLM Self-Verification
   ↓
Confidence Scoring
   ↓
Decision Engine (Safe / Unsafe / Retry)
   ↓
Final Output + Logging
```

---

## ⚙️ Tech Stack

* **Language:** Python
* **LLM API:** OpenAI
* **Orchestration:** LangGraph
* **Vector DB:** FAISS
* **Frontend:** Streamlit
* **Backend:** FastAPI (optional extension)
* **Evaluation:** Custom metrics + logging

---

## 📁 Project Structure

```
ai-guardrails-system/
│
├── app.py                    # Streamlit UI
├── main.py                   # Core pipeline
├── graph.py                  # LangGraph workflow
│
├── llm/
│   ├── generator.py
│   ├── verifier.py
│
├── safety/
│   ├── hallucination.py
│   ├── confidence.py
│   ├── filters.py
│
├── retrieval/
│   ├── retriever.py
│
├── utils/
│   ├── embeddings.py
│   ├── logger.py
│
├── evaluation/
│   ├── evaluator.py
│   ├── hallucination_eval.py
│   ├── drift.py
│   ├── dataset.json
│
└── requirements.txt
```

---

## 🧪 Example Output

```
Query: What is the capital of France?

Answer: Paris  
Confidence: High  
Similarity Score: 0.78  
Verification: YES  
Status: ✅ Safe
```

---

## 📊 Evaluation Metrics

* Hallucination Detection Accuracy
* Precision & Recall
* Safety Rate (Safe vs Unsafe outputs)
* Average Similarity Score
* Drift Detection (performance over time)

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-guardrails-system.git
cd ai-guardrails-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set API Key

```bash
export OPENAI_API_KEY="your_api_key"
```

### 4. Run Streamlit App

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

* Advanced hallucination detection using hybrid scoring
* Real-time monitoring dashboard with visual analytics
* Auto-retraining pipeline based on drift detection
* Multi-modal safety validation (text + image + audio)
* Integration with production APIs

---

## 🏆 Resume Highlights

* Built a LangGraph-based AI safety system with hallucination detection and adaptive retry logic
* Designed evaluation framework with accuracy, precision-recall, and drift monitoring
* Developed Streamlit dashboard for real-time AI response validation

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📄 License

This project is open-source and available under the MIT License.

