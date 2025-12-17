import streamlit as st

def app():
    # ==============================
    # HERO SECTION (LIGHT & PROFESSIONAL)
    # ==============================
    st.markdown("""
        <div style="
            background: linear-gradient(135deg, #B0C4DE, #E3F2FD);
            padding: 50px 20px;
            border-radius: 20px;
            color: #2C3E50;
            text-align: center;
        ">
            <h1 style="font-size:38px; margin-bottom:10px; font-weight:600;">
                Smart Microfinance Loan Assessment
            </h1>
            <p style="font-size:18px; max-width:700px; margin:auto;">
                Evaluate borrower risk, calculate EMI feasibility, and predict loan repayment
                — all in one intelligent platform.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ==============================
    # HOW IT WORKS (STEP FLOW)
    # ==============================
    st.markdown("<h2 style='text-align:center; color:#2C3E50;'>How It Works</h2>", unsafe_allow_html=True)
    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    steps = [
        ("📝", "Apply", "Submit borrower and loan details securely."),
        ("📂", "Verify", "Upload and verify borrower documents."),
        ("💰", "Calculate", "Analyze EMI feasibility based on income."),
        ("📊", "Predict", "Assess repayment probability instantly.")
    ]

    for col, (icon, title, desc) in zip([col1, col2, col3, col4], steps):
        with col:
            st.markdown(f"""
                <div style="text-align:center; padding:10px;">
                    <h1 style="font-size:36px;">{icon}</h1>
                    <h4 style="margin-bottom:5px;">{title}</h4>
                    <p style="font-size:14px; color:#555;">{desc}</p>
                </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ==============================
    # TRUST / VALUE STRIP
    # ==============================
    st.markdown("""
        <div style="
            background:#F4F6F9;
            padding:25px;
            border-radius:15px;
            display:flex;
            justify-content:space-around;
            text-align:center;
            flex-wrap: wrap;
        ">
            <div style='margin:10px; min-width:90px;'>
                <h2>⚡</h2>
                <p style='margin:0; font-size:14px;'>Fast Decisions</p>
            </div>
            <div style='margin:10px; min-width:90px;'>
                <h2>🔐</h2>
                <p style='margin:0; font-size:14px;'>Secure Data</p>
            </div>
            <div style='margin:10px; min-width:90px;'>
                <h2>📈</h2>
                <p style='margin:0; font-size:14px;'>Data-Driven</p>
            </div>
            <div style='margin:10px; min-width:90px;'>
                <h2>🏦</h2>
                <p style='margin:0; font-size:14px;'>Microfinance Ready</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ==============================
    # PRIMARY CTA
    # ==============================
    col_cta = st.columns([1, 2, 1])[1]

    with col_cta:
        if st.button("🚀 Apply for Loan"):
            st.session_state.page = "Login"
            st.rerun()
