from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains import create_sql_query_chain
from langchain_core.prompts import PromptTemplate

# 1. Connect to our SQLite file
db = SQLDatabase.from_uri("sqlite:///company_data.db")

# 2. Setup the LLM (Gemini) with zero temperature for deterministic outputs
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# 3. Create the Text-to-SQL Chain
chain = create_sql_query_chain(llm, db)

# 4. Create the Synthesis Chain (NEW)
synthesis_prompt = PromptTemplate.from_template(
    """You are a professional corporate data analyst.
    Based on the user's question, the SQL query executed, and the raw database result, provide a clear, conversational answer.
    Deliver the final insight confidently. Do not mention the SQL code in your natural response.

    User Question: {question}
    SQL Query: {query}
    Raw Result: {result}

    Executive Insight:"""
)
synthesis_chain = synthesis_prompt | llm

def get_sql_answer(user_question):
    # Generate the SQL query
    sql_query = chain.invoke({"question": user_question})
    
    # --- BULLETPROOF CLEANING STEP ---
    # 1. Clean classic markdown backticks if present
    if sql_query.startswith("```"):
        lines = sql_query.splitlines()
        clean_lines = [line for line in lines if not line.strip().startswith("```")]
        sql_query = "\n".join(clean_lines).strip()
    
    # 2. Clean text prefixes like "SQLQuery:" or "sql:"
    if sql_query.upper().startswith("SQLQUERY:"):
        sql_query = sql_query[len("SQLQuery:") :].strip()
    elif sql_query.upper().startswith("SQL:"):
        sql_query = sql_query[len("SQL:") :].strip()
        
    sql_query = sql_query.strip()
    # ----------------------------------
    
    # Execute the cleaned query
    result = db.run(sql_query)
    
    # Synthesize the final human-readable answer
    final_answer = synthesis_chain.invoke({
        "question": user_question,
        "query": sql_query,
        "result": result
    })
    
    return sql_query, result, final_answer.content