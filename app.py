import os
import tempfile
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from rag_engine import process_pdf, query_rag

# --- Page Configuration ---
st.set_page_config(page_title="InsightEngine Data Suite", page_icon="🛠️", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.title("🛠️ InsightEngine Operations")
    st.write("Logged in as active manager.")
    if st.button("Log Out"):
        st.session_state.clear()
        st.rerun()

# --- Main Interface ---
st.markdown("### Upload internal company documents and process semantic vector queries instantly.")

# 1. File Uploader
uploaded_file = st.file_uploader("Drop corporate PDFs here", type=["pdf"])

if uploaded_file is not None:
    # Check if this is a newly uploaded file so we don't re-process unnecessarily
    if "last_uploaded_file" not in st.session_state or st.session_state.last_uploaded_file != uploaded_file.name:
        
        # Save the uploaded file to a temporary location so PyPDFLoader can read it
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            temp_path = tmp_file.name
            
        with st.spinner("Processing document embeddings locally..."):
            # Process the PDF and store the vector index in session state
            st.session_state.vector_store = process_pdf(temp_path)
            
            # Mark this file as processed and clear any old chat history
            st.session_state.last_uploaded_file = uploaded_file.name
            st.session_state.chat_history = []
            
        # Clean up the temporary file from the hard drive
        os.remove(temp_path)

# 2. Chat Interface
if "vector_store" in st.session_state and st.session_state.vector_store is not None:
    st.success("Document analyzed and fully searchable!")
    
    # Initialize chat history array if it doesn't exist
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.markdown("### Ask something about your uploaded documents:")

    # Render the historical chat messages on the screen
    for message in st.session_state.chat_history:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.write(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.write(message.content)

    # Chat Input Trigger
    if user_query := st.chat_input("Type your question here..."):
        
        # Immediately display the user's new question
        with st.chat_message("user"):
            st.write(user_query)
        
        # Run the RAG pipeline and display the assistant's answer
        with st.chat_message("assistant"):
            with st.spinner("Analyzing document context..."):
                answer = query_rag(
                    st.session_state.vector_store, 
                    user_query, 
                    st.session_state.chat_history
                )
                st.write(answer)
        
        # Append the new interaction to the session state memory
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=answer))