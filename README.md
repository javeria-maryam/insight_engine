# 🚀 InsightEngine Data Suite

An enterprise-grade, end-to-end data intelligence platform that combines **Retrieval-Augmented Generation (RAG)** for unstructured document analysis with a **Conversational Text-to-SQL Engine** for structured database analytics. 

Designed with a focus on security, cost-efficiency, and user experience, InsightEngine allows non-technical users to query complex datasets using natural language and instantly receive synthesized text, dynamic visualizations, and exportable reports.

## ✨ Key Features

* **🔒 Secure Authentication Portal:** A protected access layer ensuring only authorized users can query sensitive business data and documents.
* **📄 Zero-Cost Local RAG Pipeline:** Processes and queries unstructured PDF documents using locally embedded vector processing, entirely bypassing expensive API rate limits and token costs.
* **🗄️ Conversational Text-to-SQL Engine:** Translates plain English questions into complex SQL queries, executes them against the database, and synthesizes the raw arrays into executive-friendly summaries.
* **📊 Dynamic Data Visualization:** Automatically analyzes SQL query results and renders native, interactive charts (bar charts, dataframes) based on the structural shape of the returned data.
* **📥 One-Click Data Export:** Seamlessly converts analytical results into downloadable CSV reports for external use in Excel or downstream business intelligence tools.

## 🛠️ Architecture & Tech Stack

InsightEngine is built using a modern, scalable AI engineering stack:

* **Frontend:** Streamlit (Python-based UI for rapid dashboard prototyping)
* **Orchestration:** LangChain (Managing LLM chains, prompts, and database agents)
* **Data Processing:** Pandas & AST (Dynamic string-to-dataframe conversion for visualization)
* **Database:** SQLite (Local structured data storage)
* **AI/LLM Integration:** Hybrid approach utilizing local embeddings for cost-free document processing and secure LLM API integration for advanced SQL generation.

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/insight_engine.git](https://github.com/YOUR_USERNAME/insight_engine.git)
   cd insight_engine
Create a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
streamlit run app.py
🧠 The Engineering Philosophy
This project was built to demonstrate that applied AI engineering is about Systems Orchestration, not just model training. By wiring together an LLM, a vector database, a SQL execution engine, and a frontend framework with custom error-handling parsers, InsightEngine bridges the gap between raw data and actionable business intelligence.

Special attention was given to edge-case handling, such as building custom parsers to strip rogue markdown formatting from LLM SQL outputs before database execution.

🔮 Future Roadmap (v2.0)
Cloud Deployment: Migration from localhost to a live cloud environment (AWS/Render).

Production Database Integration: Transitioning the storage layer from local SQLite to PostgreSQL.

Hybrid Search: Implementing advanced retrieval combining vector embeddings with BM25 keyword search for maximum document accuracy.

Developed as a portfolio piece showcasing applied AI architecture and data engineering.


***

### How to push this to your repository:

1. Create a file named `README.md` in your project folder.
2. Paste the code above into it. (Make sure to swap out `YOUR_USERNAME` in the clone link with your actual GitHub username!)
3. Run your standard push commands:
   ```bash
   git add README.md
   git commit -m "docs: add master README for project portfolio presentation"
   git push