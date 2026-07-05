import os
import tempfile
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from rag_engine import process_pdf, query_rag
from sql_engine import get_sql_answer

# --- Page Configuration ---
st.set_page_config(page_title="InsightEngine Data Suite", page_icon="🛠️", layout="wide")

# --- Day 1: Authentication System ---
# --- Day 1: Authentication System (Upgraded) ---
def check_password():
    """Returns True if the user enters the correct username and password."""
    def login_callback():
        # Verifying both credentials
        if (st.session_state["username_input"] == "admin" and 
            st.session_state["password_input"] == "admin123"):
            st.session_state["password_correct"] = True
            # Flush credentials from active session state memory for security
            del st.session_state["username_input"]
            del st.session_state["password_input"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.title("🔒 Security Portal")
        st.text_input("Username", key="username_input")
        st.text_input("Password", type="password", key="password_input")
        st.button("Login", on_click=login_callback)
        return False
    elif not st.session_state["password_correct"]:
        st.title("🔒 Security Portal")
        st.text_input("Username", key="username_input")
        st.text_input("Password", type="password", key="password_input")
        st.button("Login", on_click=login_callback)
        st.error("❌ Incorrect credentials. Please try again.")
        return False
    return True

# --- Main Application Gate ---
if check_password():
    st.title("🛠️ InsightEngine Data Suite")
    
    # Create the navigation tabs
    tab1, tab2 = st.tabs(["📄 Document Auditor", "📊 SQL Analytics"])

    # --- TAB 1: Document Auditor ---
    with tab1:
        st.markdown("### Upload internal company documents.")
        uploaded_file = st.file_uploader("Drop corporate PDFs here", type=["pdf"])
        
        if uploaded_file:
            if "last_uploaded_file" not in st.session_state or st.session_state.last_uploaded_file != uploaded_file.name:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded_file.getvalue())
                    path = tmp.name
                st.session_state.vector_store = process_pdf(path)
                st.session_state.last_uploaded_file = uploaded_file.name
                st.session_state.chat_history = []
                os.remove(path)

        if "vector_store" in st.session_state:
            st.success("Document analyzed!")
            
            # Render chat history
            if "chat_history" in st.session_state:
                for message in st.session_state.chat_history:
                    if isinstance(message, HumanMessage):
                        with st.chat_message("user"): st.write(message.content)
                    elif isinstance(message, AIMessage):
                        with st.chat_message("assistant"): st.write(message.content)
            
            if user_query := st.chat_input("Ask about the documents..."):
                with st.chat_message("user"): st.write(user_query)
                with st.chat_message("assistant"):
                    answer = query_rag(st.session_state.vector_store, user_query, st.session_state.chat_history)
                    st.write(answer)
                st.session_state.chat_history.append(HumanMessage(content=user_query))
                st.session_state.chat_history.append(AIMessage(content=answer))

    # --- TAB 2: SQL Analytics ---
    # --- TAB 2: SQL Analytics ---
    with tab2:
        st.markdown("### Query your SQL Database")
        st.write("Try asking: *'What was the total revenue for Cloud Storage?'* or *'Which product generated the most revenue?'*")
        
        if sql_query := st.chat_input("Ask a question about the database...", key="sql_input"):
            with st.chat_message("user"):
                st.write(sql_query)
                
            with st.spinner("Translating to SQL and analyzing data..."):
                # Unpack the three return values
                query, raw_result, insight = get_sql_answer(sql_query)
                
            with st.chat_message("assistant"):
                # Display the clean, synthesized AI response
                st.markdown(f"**Insight:** {insight}")
                
                # Tuck the raw data and SQL inside a collapsible expander
                with st.expander("🔍 View Technical Details"):
                    st.code(query, language="sql")
                    st.write(f"**Raw Array:** `{raw_result}`")