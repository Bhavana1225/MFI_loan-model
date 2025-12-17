from ui import load_ui
load_ui()
import streamlit as st
import Home, Login, Register, CustomerDetails, DocumentUpload, EMI, Prediction, About

st.set_page_config(page_title="Microfinance Loan App", layout="wide")

# -----------------------------
# Session State Init
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

# -----------------------------
# Sidebar Navigation
# -----------------------------
pages = [
    "Home",
    "Login",
    "Register",
    "Customer Details",
    "Document Upload",
    "EMI Calculator",
    "Prediction",
    "About"
]

selected_page = st.sidebar.radio(
    "",
    pages,
    index=pages.index(st.session_state.page)
)

# Sync sidebar → page
st.session_state.page = selected_page

# -----------------------------
# Page Routing
# -----------------------------
page = st.session_state.page

if page == "Home":
    Home.app()

elif page == "Login":
    Login.app()

elif page == "Register":
    Register.app()

elif page == "Customer Details":
    CustomerDetails.app()

elif page == "Document Upload":
    DocumentUpload.app()

elif page == "EMI Calculator":
    EMI.app()

elif page == "Prediction":
    Prediction.app()

elif page == "About":
    About.app()
