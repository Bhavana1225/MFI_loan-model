import streamlit as st
import Home
import Prediction
import About

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Microfinance Loan App", layout="wide")

# -----------------------------
# Sidebar Navigation (Mobile-Friendly)
# -----------------------------
# Wrap radio buttons in a responsive div
st.markdown("""
<style>
/* Sidebar full width on small screens */
@media only screen and (max-width: 600px) {
    .css-1d391kg {   /* Streamlit sidebar container */
        width: 100% !important;
        min-width: 100% !important;
    }
    .css-1d391kg .stRadio { 
        width: 100% !important;
    }
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Explore Sections")
page = st.sidebar.radio("Go to", ["Home", "Prediction", "About"])

# -----------------------------
# Display Selected Page
# -----------------------------
if page == "Home":
    Home.app()
elif page == "Prediction":
    Prediction.app()
else:
    About.app()
