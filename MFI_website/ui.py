import streamlit as st

def load_ui():
    st.markdown("""
    <style>

    /* =============================
       REMOVE WHITE TOP STRIP
    ============================= */

    header {
        background-color: #F4F6F9 !important;
    }

    [data-testid="stToolbar"] {
        background-color: #F4F6F9 !important;
    }

    /* Keep hamburger visible */
    header * {
        color: #2C3E50 !important;
    }

    /* =============================
       APP BACKGROUND
    ============================= */

    html, body, .stApp {
        background-color: #F4F6F9 !important;
    }

    .block-container {
        background-color: #F4F6F9 !important;
        padding-top: 1rem !important;
    }

    /* =============================
       SIDEBAR STYLE
    ============================= */

    section[data-testid="stSidebar"] {
        background-color: #ECF0F1 !important;
        border-right: 1px solid #D5D8DC;
    }

    section[data-testid="stSidebar"] * {
        color: #2C3E50 !important;
        font-weight: 500;
    }

    /* Remove sidebar heading text */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        display: none;
    }

    /* =============================
       UNIFORM SIDEBAR ITEMS
    ============================= */

    div[role="radiogroup"] label {
        background-color: #FFFFFF;
        padding: 12px 14px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid #DADDE2;
        display: flex;
        align-items: center;
        height: 48px;
        font-size: 15px;
        cursor: pointer;
    }

    div[role="radiogroup"] label:hover {
        background-color: #D6EAF8;
    }

    div[role="radiogroup"] input {
        margin-right: 10px;
    }

    /* =============================
       BUTTONS
    ============================= */

    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 48px;
        font-size: 16px;
        font-weight: 600;
        background-color: #2E86C1;
        color: white;
        border: none;
    }

    .stButton > button:hover {
        background-color: #1B4F72;
    }

    /* =============================
       MOBILE FIX
    ============================= */

    @media (max-width: 768px) {
        .block-container {
            padding: 0.6rem !important;
        }
        div[role="radiogroup"] label {
            height: 44px;
            font-size: 14px;
        }
    }

    </style>
    """, unsafe_allow_html=True)
