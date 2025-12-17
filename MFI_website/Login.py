import streamlit as st
import json
import os

# -----------------------------
# JSON file to store users
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_FILE = os.path.join(BASE_DIR, "users.json")

# -----------------------------
# Main Login App
# -----------------------------
def app():
    st.title("🔐 Login")

    # -----------------------------
    # Load users safely
    # -----------------------------
    if "users" not in st.session_state:
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r") as f:
                st.session_state.users = json.load(f)
        else:
            st.session_state.users = {}

    # -----------------------------
    # Persistent input fields
    # -----------------------------
    for key in ["login_email","login_password"]:
        if key not in st.session_state:
            st.session_state[key] = ""

    st.session_state.login_email = st.text_input("Email", value=st.session_state.login_email)
    st.session_state.login_password = st.text_input("Password", type="password", value=st.session_state.login_password)

    # -----------------------------
    # Login logic
    # -----------------------------
    if st.button("Login"):
        email = st.session_state.login_email.strip()
        password = st.session_state.login_password.strip()

        if email in st.session_state.users and st.session_state.users[email]["password"] == password:
            st.success("Login successful ✅")
            st.session_state.logged_in = True
            st.session_state.current_user = email  # store current logged-in user
            st.session_state.page = "Customer Details"  # redirect after login
            st.rerun()
        else:
            st.error("❌ Invalid credentials")

    st.write("---")
    st.write("Not registered yet?")

    if st.button("📝 Go to Register"):
        st.session_state.page = "Register"
        st.rerun()
