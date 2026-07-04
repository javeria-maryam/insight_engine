import streamlit as st

# Local portfolio credentials (username: password)
USER_CREDENTIALS = {
    "admin": "password123",
    "client": "demo2026"
}

def check_password():
    """Returns True if the user has provided valid credentials."""
    # Step 1: Initialize session state if it doesn't exist yet
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    # Step 2: If already logged in, skip the form
    if st.session_state.authenticated:
        return True

    # Step 3: Show the security login layout
    st.title("🔒 InsightEngine Secure Login")
    st.write("Welcome to the corporate business intelligence portal.")
    
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")
    
    if st.button("Log In"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state.authenticated = True
            st.success("Access Granted!")
            st.rerun()  # Refresh the page to show the dashboard
        else:
            st.error("❌ Invalid Username or Password")
            
    return False