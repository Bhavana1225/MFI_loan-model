import streamlit as st
import json
import os

# -----------------------------
# JSON file to store users
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_FILE = os.path.join(BASE_DIR, "users.json")

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
# Main Register App
# -----------------------------
def app():
    st.title("📝 Register")

    # Using a form ensures all inputs are captured together
    with st.form("register_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm = st.text_input("Confirm Password", type="password")

        submitted = st.form_submit_button("Register")

        if submitted:
            # Strip whitespace
            name = name.strip()
            email = email.strip()
            password = password.strip()
            confirm = confirm.strip()

            if not name or not email or not password or not confirm:
                st.error("❌ All fields are required")
            elif password != confirm:
                st.error("❌ Passwords do not match")
            elif email in st.session_state.users:
                st.warning("⚠ User already exists")
            else:
                # Save to session_state
                st.session_state.users[email] = {
                    "name": name,
                    "password": password
                }

                # Persist users to file
                with open(USERS_FILE, "w") as f:
                    json.dump(st.session_state.users, f, indent=4)

                st.success("✅ Registration successful")
                st.session_state.page = "Login"
                st.rerun()
