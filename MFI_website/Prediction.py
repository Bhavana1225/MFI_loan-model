import streamlit as st
import pandas as pd
from catboost import CatBoostClassifier, Pool
import os

# Load trained model safely (works locally + Streamlit Cloud)
model = CatBoostClassifier()
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "catboost_model.cbm")
model.load_model(model_path)

# Feature list used during training
FEATURES = [
    "msisdn", "aon", "daily_decr30", "daily_decr90", "rental30", "rental90",
    "last_rech_date_ma", "last_rech_date_da", "last_rech_amt_ma", "cnt_ma_rech30",
    "fr_ma_rech30", "sumamnt_ma_rech30", "medianamnt_ma_rech30", "medianmarechprebal30",
    "cnt_ma_rech90", "fr_ma_rech90", "sumamnt_ma_rech90", "medianamnt_ma_rech90",
    "medianmarechprebal90", "cnt_da_rech30", "fr_da_rech30", "cnt_da_rech90", "fr_da_rech90",
    "cnt_loans30", "amnt_loans30", "maxamnt_loans30", "medianamnt_loans30",
    "cnt_loans90", "amnt_loans90", "maxamnt_loans90", "medianamnt_loans90",
    "payback30", "payback90", "pcircle", "pdate"
]

CAT_FEATURES = ["pcircle"]


def predict_loan(monthly_income, loan_amount):
    if loan_amount > (10 * monthly_income):
        return 0.0, "❌ Loan amount too high compared to income."

    data = [{
        "msisdn": 0,
        "aon": monthly_income,
        "daily_decr30": loan_amount * 0.1,
        "daily_decr90": loan_amount * 0.15,
        "rental30": 1000,
        "rental90": 3000,
        "last_rech_date_ma": 10,
        "last_rech_date_da": 5,
        "last_rech_amt_ma": 200,
        "cnt_ma_rech30": 2,
        "fr_ma_rech30": 0.5,
        "sumamnt_ma_rech30": 500,
        "medianamnt_ma_rech30": 250,
        "medianmarechprebal30": 100,
        "cnt_ma_rech90": 4,
        "fr_ma_rech90": 0.7,
        "sumamnt_ma_rech90": 1200,
        "medianamnt_ma_rech90": 300,
        "medianmarechprebal90": 200,
        "cnt_da_rech30": 1,
        "fr_da_rech30": 0.2,
        "cnt_da_rech90": 3,
        "fr_da_rech90": 0.6,
        "cnt_loans30": 1,
        "amnt_loans30": 500,
        "maxamnt_loans30": 500,
        "medianamnt_loans30": 500,
        "cnt_loans90": 2,
        "amnt_loans90": 1000,
        "maxamnt_loans90": 1000,
        "medianamnt_loans90": 500,
        "payback30": 1,
        "payback90": 1,
        "pcircle": "UPW",
        "pdate": 20160720
    }]

    df = pd.DataFrame(data, columns=FEATURES)
    pool = Pool(df, cat_features=CAT_FEATURES)

    prob = model.predict_proba(pool)[0][1]
    decision = "✅ Loan can be given" if prob > 0.5 else "❌ Loan should NOT be given"

    return prob, decision


def app():
    st.markdown("<h1 style='color:#4A6EE0;'>🔮 Loan Repayment Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#444; font-size:17px;'>Enter the loan details below to check borrower repayment probability.</p>", unsafe_allow_html=True)

    loan_amount = st.number_input("💵 Loan Amount", min_value=0.0, step=100.0)
    monthly_income = st.number_input("📈 Monthly Income", min_value=0.0, step=100.0)

    # Modern Predict button styling
    button_html = """
    <style>
    .stButton>button {
        background-color: #4A6EE0;
        color: white;
        font-size:16px;
        border-radius:10px;
        padding:8px 20px;
        width:120px;
    }
    .stButton>button:hover {
        background-color: #3B57B1;
        color: white;
    }
    </style>
    """
    st.markdown(button_html, unsafe_allow_html=True)

    if st.button("Predict"):
        prob, decision = predict_loan(monthly_income, loan_amount)
        st.markdown(f"<h2>{decision}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:20px;'>Repayment Probability: <b>{prob:.4f}</b></p>", unsafe_allow_html=True)
