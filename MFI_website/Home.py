import streamlit as st

def app():
    st.markdown("""
        <h1 style='text-align:center; color:#4A6EE0;'>💰 Microfinance Loan Project</h1>
        <p style='text-align:center; font-size:18px; color:#444;'>
            Predict loan repayment probabilities quickly and efficiently.
        </p>
        <br>
    """, unsafe_allow_html=True)

    # Responsive columns: stack on small screens
    col1, col2, col3 = st.columns([1,1,1], gap="small")

    with col1:
        st.markdown("""
            <div style='background:#E3F2FD; padding:20px; border-radius:12px; text-align:center; max-width:100%;'>
                <h2>📊 Prediction</h2>
                <p>Check whether a borrower is likely to repay a loan.</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style='background:#FFF3E0; padding:20px; border-radius:12px; text-align:center; max-width:100%;'>
                <h2>📁 Data Insights</h2>
                <p>Uses borrower behavioral and telecom data for analysis.</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div style='background:#E8F5E9; padding:20px; border-radius:12px; text-align:center; max-width:100%;'>
                <h2>📖 Overview</h2>
                <p>Helps microfinance teams make informed lending decisions.</p>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.markdown("<h3 style='text-align:center;'>Discover what the app can do 💡</h3>", unsafe_allow_html=True)
