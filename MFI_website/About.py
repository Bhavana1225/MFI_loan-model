import streamlit as st

def app():
    # ==============================
    # HEADER
    # ==============================
    st.markdown("""
        <div style="text-align:center; padding:10px 0;">
            <h1 style="color:#4A6EE0; font-size:42px;">ℹ️ About This Application</h1>
            <p style="font-size:18px; color:#555; max-width:800px; margin:auto;">
                A smart microfinance decision-support system designed to assess loan repayment risk
                using borrower behavioral and telecom indicators.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ==============================
    # FEATURE CARDS
    # ==============================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div style="background:#E3F2FD; padding:22px; border-radius:16px; height:100%;">
                <h3>📊 Risk Prediction</h3>
                <p style="font-size:16px; color:#444;">
                    Estimates whether a borrower is likely to repay a loan based on historical
                    behavioral trends and usage patterns.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="background:#E8F5E9; padding:22px; border-radius:16px; height:100%;">
                <h3>📁 Data-Driven Insights</h3>
                <p style="font-size:16px; color:#444;">
                    Leverages telecom activity, recharge frequency, and borrower behavior
                    to generate meaningful credit insights.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div style="background:#FFF3E0; padding:22px; border-radius:16px; height:100%;">
                <h3>⚖️ Smarter Decisions</h3>
                <p style="font-size:16px; color:#444;">
                    Helps microfinance institutions reduce default risk and make
                    confident, informed lending decisions.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ==============================
    # PURPOSE SECTION
    # ==============================
    st.markdown("""
        <div style="background:#F4F6F9; padding:25px; border-radius:18px;">
            <h2 style="color:#2C3E50;">🎯 Purpose of the System</h2>
            <p style="font-size:17px; color:#444;">
                This application is designed to support microfinance teams by providing
                a transparent and easy-to-use platform for assessing borrower creditworthiness.
                By combining borrower details, EMI feasibility, and predictive analytics,
                the system improves lending efficiency while minimizing financial risk.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ==============================
    # FOOTER NOTE
    # ==============================
    st.markdown("""
        <p style="text-align:center; color:#777; font-size:14px;">
            Built to empower microfinance institutions with intelligent, data-driven loan decisions.
        </p>
    """, unsafe_allow_html=True)
