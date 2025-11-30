import streamlit as st

def app():
    st.markdown("<h1 style='color:#4A6EE0;'>ℹ️ About This Project</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:17px; color:#444;'>This project helps microfinance institutions estimate loan repayment likelihood using borrower telecom and behavioral indicators.</p>", unsafe_allow_html=True)

    st.markdown("""
        <div style='background:#F3E5F5; padding:20px; border-radius:12px;'>
            <h3>📌 What It Does</h3>
            <ul style='font-size:17px;'>
                <li>Predicts whether a borrower is likely to repay a loan.</li>
                <li>Uses historical recharge and behavioral patterns.</li>
                <li>Supports informed microfinance lending decisions.</li>
            </ul>
        </div>

        <br>

        <div style='background:#E3F2FD; padding:20px; border-radius:12px;'>
            <h3>🎯 Purpose</h3>
            <p>This tool provides microfinance teams with a clear way to analyze risk and borrower behavior.</p>
        </div>
    """, unsafe_allow_html=True)
