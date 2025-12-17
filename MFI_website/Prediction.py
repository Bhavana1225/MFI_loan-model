import streamlit as st
import pandas as pd
from catboost import CatBoostClassifier, Pool
import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import date

# -----------------------------
# Load CatBoost model
# -----------------------------
model = CatBoostClassifier()
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "catboost_model.cbm")
model.load_model(model_path)

FEATURES = [
    "msisdn","aon","daily_decr30","daily_decr90","rental30","rental90",
    "last_rech_date_ma","last_rech_date_da","last_rech_amt_ma","cnt_ma_rech30",
    "fr_ma_rech30","sumamnt_ma_rech30","medianamnt_ma_rech30","medianmarechprebal30",
    "cnt_ma_rech90","fr_ma_rech90","sumamnt_ma_rech90","medianamnt_ma_rech90",
    "medianmarechprebal90","cnt_da_rech30","fr_da_rech30","cnt_da_rech90","fr_da_rech90",
    "cnt_loans30","amnt_loans30","maxamnt_loans30","medianamnt_loans30",
    "cnt_loans90","amnt_loans90","maxamnt_loans90","medianamnt_loans90",
    "payback30","payback90","pcircle","pdate"
]

CAT_FEATURES = ["pcircle"]

# -----------------------------
# Prediction logic
# -----------------------------
def predict_loan(monthly_income, loan_amount):
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
    return model.predict_proba(pool)[0][1]

# -----------------------------
# PDF REPORT (BLANK SIGN & SEAL)
# -----------------------------
def generate_report(customer, emi, decision, reason, risk):
    file_name = "Loan_Assessment_Report.pdf"
    doc = SimpleDocTemplate(
        file_name,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("<b>MICROFINANCE LOAN ASSESSMENT REPORT</b>", styles["Title"]))
    content.append(Spacer(1, 10))
    content.append(Paragraph("<b>Credit Evaluation Document</b>", styles["Normal"]))
    content.append(Paragraph(f"Report Date: {date.today()}", styles["Normal"]))
    content.append(Spacer(1, 20))

    content.append(Paragraph("<b>1. Applicant Information</b>", styles["Heading2"]))
    content.append(Spacer(1, 8))

    table1 = Table([
        ["Applicant Name", customer["name"]],
        ["Age", customer["age"]],
        ["Monthly Income", f"₹ {customer['monthly_income']}"],
        ["Loan Amount Requested", f"₹ {customer['loan_amount']}"],
        ["Credit History", customer["credit_history"]],
    ], colWidths=[200, 280])

    table1.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
    ]))

    content.append(table1)
    content.append(Spacer(1, 20))

    content.append(Paragraph("<b>2. EMI & Repayment Analysis</b>", styles["Heading2"]))
    content.append(Spacer(1, 8))

    table2 = Table([
        ["Interest Rate", "5% per annum"],
        ["Recommended EMI", f"₹ {emi['recommended_emi']}"],
        ["Monthly Capacity", f"₹ {emi['monthly_capacity']}"],
        ["Repayment Period", f"{emi['repayment_months']} months"],
    ], colWidths=[200, 280])

    table2.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
    ]))

    content.append(table2)
    content.append(Spacer(1, 20))

    content.append(Paragraph("<b>3. Risk & Decision</b>", styles["Heading2"]))
    content.append(Paragraph(f"Predicted Risk Score: {risk:.2f}%", styles["Normal"]))
    content.append(Paragraph(f"Decision: <b>{decision}</b>", styles["Normal"]))
    content.append(Paragraph(f"Reason: {reason}", styles["Normal"]))
    content.append(Spacer(1, 30))

    content.append(Paragraph("<b>Authorized Verification</b>", styles["Heading2"]))
    content.append(Spacer(1, 30))
    content.append(Paragraph("Signature: ________________________________", styles["Normal"]))
    content.append(Spacer(1, 20))
    content.append(Paragraph("Seal / Stamp: ____________________________", styles["Normal"]))

    doc.build(content)
    return file_name

# -----------------------------
# Main App
# -----------------------------
def app():
    st.markdown("<h1 style='color:#2E86C1;'>📊 Loan Risk Assessment</h1>", unsafe_allow_html=True)

    if not st.session_state.get("logged_in"):
        st.warning("⚠ Please log in.")
        return

    if not st.session_state.get("documents_verified"):
        st.warning("⚠ Documents not verified.")
        return

    customer = st.session_state.get("customer_data")
    emi = st.session_state.get("emi_data")

    if not customer or not emi:
        st.warning("⚠ Missing customer or EMI data.")
        return

    st.subheader("👤 Customer Summary")
    st.table(customer)

    prob = predict_loan(customer["monthly_income"], customer["loan_amount"])
    risk = (1 - prob) * 100

    decision = "APPROVED"
    reason = "All eligibility criteria satisfied."

    if customer["age"] < 21:
        decision = "REJECTED"
        reason = "Applicant age below minimum eligibility."
    elif emi["monthly_capacity"] > customer["monthly_income"] * 0.6:
        decision = "REJECTED"
        reason = "EMI not affordable."
    elif customer["credit_history"] == "Poor":
        decision = "REJECTED"
        reason = "Poor credit history."
    elif risk > 70:
        decision = "REJECTED"
        reason = "High default risk."

    st.subheader("📌 Final Decision")

    if decision == "APPROVED":
        st.success(f"✅ LOAN APPROVED ({risk:.2f}% Risk)")
    else:
        st.error(f"❌ LOAN REJECTED ({risk:.2f}% Risk)")

    st.markdown(f"**Reason:** {reason}")

    report = generate_report(customer, emi, decision, reason, risk)

    with open(report, "rb") as f:
        st.download_button(
            "📄 Download Loan Assessment Report",
            f,
            file_name=report,
            mime="application/pdf"
        )
