import streamlit as st
from main import run_pipeline

st.set_page_config(page_title="AI Guardrails System", layout="wide")

st.title("🛡️ AI Safety & Guardrails Dashboard")

st.markdown("Evaluate LLM responses with hallucination detection, confidence scoring, and verification.")

query = st.text_input("Ask a question : ")

if st.button("Run AI Pipeline"):
    if query:
        with st.spinner("Processing..."):
            result = run_pipeline(query)
        
        st.subheader("📌 Results")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🧠 Answer")
            st.success(result["answer"])

            st.markdown("### 📊 Confidence")
            st.info(result["confidence"])

        with col2:
            st.markdown("### 🔍 Similarity Score")
            st.write(result["similarity_score"])

            st.markdown("### ✅ Verification")
            st.write(result["verification"])

        st.markdown("### 🚦 Safety Status")

        if "Safe" in result["status"]:
            st.success(result["status"])
        elif "Low" in result["status"]:
            st.warning(result["status"])
        else:
            st.error(result["status"])

    else:
        st.warning("Please enter a query.")