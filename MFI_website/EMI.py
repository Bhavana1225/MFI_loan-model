import streamlit as st
import math

def app():
    st.title("💰 EMI Calculator & Repayment Plan")

    # -----------------------------
    # Login & Document Check
    # -----------------------------
    if not st.session_state.get("logged_in"):
        st.warning("⚠ Please log in to access EMI Calculator.")
        return

    if not st.session_state.get("documents_verified"):
        st.warning("⚠ Please complete document verification first.")
        return

    if "customer_data" not in st.session_state:
        st.warning("⚠ Customer details missing.")
        return

    customer = st.session_state.customer_data
    loan_amount = customer.get("loan_amount", 0)
    monthly_income = customer.get("monthly_income", 0)

    st.info(f"**Requested Loan Amount:** ₹{loan_amount}")
    st.info(f"**Monthly Income:** ₹{monthly_income}")

    # -----------------------------
    # Fixed Interest Rate (5%)
    # -----------------------------
    interest_rate = 5.0
    st.info("**Fixed Annual Interest Rate:** 5%")

    monthly_capacity = st.number_input(
        "How much can you pay per month (₹)?",
        min_value=500,
        step=500
    )

    # -----------------------------
    # STEP 1: Calculate EMI
    # -----------------------------
    if st.button("Calculate EMI"):
        monthly_rate = interest_rate / (12 * 100)

        recommended_emi = loan_amount * monthly_rate * (1 + monthly_rate) ** 12 / ((1 + monthly_rate) ** 12 - 1)

        if monthly_capacity <= loan_amount * monthly_rate:
            st.error("❌ Monthly amount too low. Loan will never close.")
            return

        months_needed = math.ceil(
            math.log(monthly_capacity / (monthly_capacity - loan_amount * monthly_rate))
            / math.log(1 + monthly_rate)
        )

        total_payable = months_needed * monthly_capacity

        # Save EMI data
        st.session_state.emi_data = {
            "loan_amount": loan_amount,
            "interest_rate": interest_rate,
            "monthly_capacity": monthly_capacity,
            "recommended_emi": round(recommended_emi, 2),
            "repayment_months": months_needed,
            "total_payable": total_payable
        }

        st.session_state.emi_calculated = True

    # -----------------------------
    # STEP 2: Show EMI Results
    # -----------------------------
    if st.session_state.get("emi_calculated"):
        emi = st.session_state.emi_data

        st.success("✅ EMI calculation completed")

        st.markdown("### 📊 Repayment Summary")
        st.write(f"**Recommended EMI (12 months @ 5%):** ₹{emi['recommended_emi']}")
        st.write(f"**Your Monthly Payment:** ₹{emi['monthly_capacity']}")
        st.write(f"**Expected Repayment Duration:** {emi['repayment_months']} months")
        st.write(f"**Total Payable (approx):** ₹{emi['total_payable']}")

        st.divider()

        # -----------------------------
        # STEP 3: Redirect Button
        # -----------------------------
        if st.button("Proceed to Loan Assessment"):
            st.session_state.page = "Prediction"
            st.session_state.sidebar_page = "Prediction"  # ✅ ONLY FIX
            st.rerun()
