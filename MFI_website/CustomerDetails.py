import streamlit as st

def app():
    st.title("Customer / Applicant Details")

    # -----------------------------
    # Login Check
    # -----------------------------
    if not st.session_state.get("logged_in"):
        st.warning("⚠ You must be logged in to enter customer details.")
        return

    # -----------------------------
    # Load saved data (persistence)
    # -----------------------------
    if "customer_data" not in st.session_state:
        st.session_state.customer_data = {}

    customer_data = st.session_state.customer_data

    # -----------------------------
    # Use a form for reliable submission
    # -----------------------------
    with st.form("customer_form"):
        # Personal Info
        name = st.text_input("Full Name", value=customer_data.get("name", ""))
        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            step=1,
            value=customer_data.get("age", 18)
        )
        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"],
            index=["Male", "Female", "Other"].index(customer_data.get("gender", "Male"))
        )
        marital_status = st.selectbox(
            "Marital Status",
            ["Single", "Married", "Other"],
            index=["Single", "Married", "Other"].index(customer_data.get("marital_status", "Single"))
        )

        # Contact Info
        email = st.text_input("Email", value=customer_data.get("email", ""))
        phone = st.text_input("Phone Number", value=customer_data.get("phone", ""))

        # Financial Info
        occupation = st.selectbox(
            "Occupation",
            ["Salaried", "Self-Employed", "Unemployed"],
            index=["Salaried", "Self-Employed", "Unemployed"].index(customer_data.get("occupation", "Salaried"))
        )
        monthly_income = st.number_input(
            "Monthly Income (₹)",
            min_value=0,
            step=1000,
            value=customer_data.get("monthly_income", 0)
        )
        existing_loans = st.radio(
            "Existing Loans?",
            ["Yes", "No"],
            index=["Yes", "No"].index(customer_data.get("existing_loans", "No"))
        )
        credit_history = st.selectbox(
            "Credit History",
            ["Good", "Average", "Poor"],
            index=["Good", "Average", "Poor"].index(customer_data.get("credit_history", "Good"))
        )
        loan_amount = st.number_input(
            "Loan Amount Requested (₹)",
            min_value=0,
            step=1000,
            value=customer_data.get("loan_amount", 0)
        )
        loan_purpose = st.selectbox(
            "Loan Purpose",
            ["Business", "Education", "Personal", "Other"],
            index=["Business", "Education", "Personal", "Other"].index(customer_data.get("loan_purpose", "Business"))
        )

        # Extra Info
        years_employed = st.number_input(
            "Years of Employment",
            min_value=0,
            max_value=50,
            step=1,
            value=customer_data.get("years_employed", 0)
        )
        collateral_available = st.radio(
            "Collateral Available?",
            ["Yes", "No"],
            index=["Yes", "No"].index(customer_data.get("collateral_available", "No"))
        )

        # Form submission button
        submitted = st.form_submit_button("Submit Details")

        if submitted:
            # Strip whitespace for safety
            name = name.strip()
            email = email.strip()
            phone = phone.strip()

            # Basic validation
            if not name or not email or not phone:
                st.error("❌ Name, Email, and Phone are required.")
            elif age < 18:
                st.error("❌ Applicant must be at least 18 years old.")
            elif monthly_income <= 0:
                st.error("❌ Monthly income must be greater than zero.")
            else:
                # Save data
                st.session_state.customer_data = {
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "marital_status": marital_status,
                    "email": email,
                    "phone": phone,
                    "occupation": occupation,
                    "monthly_income": monthly_income,
                    "existing_loans": existing_loans,
                    "credit_history": credit_history,
                    "loan_amount": loan_amount,
                    "loan_purpose": loan_purpose,
                    "years_employed": years_employed,
                    "collateral_available": collateral_available
                }

                # Completion flag
                st.session_state.customer_details_completed = True

                st.success("✅ Customer details saved successfully!")

                # Auto redirect to Document Upload
                st.session_state.page = "Document Upload"
                st.rerun()
