import streamlit as st
import pandas as pd
from catboost import CatBoostClassifier, Pool

# -----------------------------------------
# LOAD MODEL (same as your model)
# -----------------------------------------
model = CatBoostClassifier()
model.load_model("catboost_model.cbm")

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


# -----------------------------------------
# SHARED PREDICTION FUNCTION
# -----------------------------------------
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


st.set_page_config(page_title="Microfinance Prediction", layout="centered")
st.write("")  # empty body (no UI on main file)
