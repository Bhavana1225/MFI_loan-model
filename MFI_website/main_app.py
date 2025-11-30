import streamlit as st
import Home
import Prediction
import About

st.set_page_config(page_title="Microfinance Loan App", layout="wide")

# Sidebar Navigation
st.sidebar.title("Explore Sections")
page = st.sidebar.radio("Go to", ["Home", "Prediction", "About"])

# Display Selected Page
if page == "Home":
    Home.app()
elif page == "Prediction":
    Prediction.app()
else:
    About.app()
