# 🛠️ InsightEngine Data Suite

An enterprise-grade, hybrid Retrieval-Augmented Generation (RAG) dashboard designed for secure, high-speed corporate document auditing. InsightEngine allows users to upload dense PDFs and query them instantly using natural language, complete with conversational memory for complex follow-up questions.

## 🚀 Current Architecture (Day 2 Build)

This project utilizes a hybrid local/cloud architecture to guarantee maximum data privacy and absolute immunity to API rate limits during the embedding phase.

### Core Features
* **Secure Document Ingestion:** Processes complex corporate PDFs using `PyPDFLoader` and intelligent recursive character chunking to maintain semantic context.
* **Zero-Cost Local Embeddings:** Utilizes HuggingFace's `all-MiniLM-L6-v2` running locally on the CPU. This ensures high-volume document vectorization without hitting cloud API rate limits or incurring token costs.
* **High-Speed Vector Retrieval:** Implements a localized FAISS (Facebook AI Similarity Search) index in-memory for millisecond-latency semantic searching.
* **Conversational Memory Engine:** Features a dual-prompt LangChain pipeline that contextualizes follow-up questions against the chat history before querying the vector store, allowing for natural, continuous conversations.
* **Anti-Hallucination Guardrails:** Strictly constrained system prompts force the LLM to rely *only* on the retrieved context, admitting ignorance rather than fabricating corporate policy.
* **State-of-the-Art Text Generation:** Powered by Google's `gemini-2.5-flash` for rapid, highly accurate synthesis of the final answer.

## 💻 Tech Stack

* **Frontend:** Streamlit
* **Orchestration:** LangChain
* **Embeddings:** HuggingFace (`sentence-transformers`)
* **Vector Database:** FAISS
* **LLM Engine:** Google Gemini API (`gemini-2.5-flash`)

## ⚙️ Local Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/insight_engine.git](https://github.com/YOUR_GITHUB_USERNAME/insight_engine.git)
   cd insight_engine

Create and activate a virtual environment:

Bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

Install the required dependencies:

Bash
pip install streamlit langchain-google-genai langchain-community langchain-classic langchain-huggingface sentence-transformers faiss-cpu pypdf python-dotenv


Environment Variables:
Create a .env file in the root directory and add your Google API Key:

Plaintext
GOOGLE_API_KEY=your_api_key_here


Run the Application:

Bash
python -m streamlit run app.py

Note: This repository is currently in active development. Upcoming modules include a Text-to-SQL analytics engine for querying structured database records.

