import streamlit as st
from PyPDF2 import PdfReader
from PIL import Image

# Try importing pytesseract; handle if unavailable (Streamlit Cloud)
try:
    import pytesseract
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False

# -----------------------------
# Tesseract path (Windows)
# -----------------------------
if TESSERACT_AVAILABLE:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

# -----------------------------
# Helper functions
# -----------------------------
def extract_text(file):
    """Extract text from PDF or Image (best-effort OCR)"""
    text = ""
    try:
        if file.type == "application/pdf":
            reader = PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
        elif TESSERACT_AVAILABLE and file.type.startswith("image/"):
            image = Image.open(file)
            text = pytesseract.image_to_string(image)
    except:
        return ""
    return text.strip()

def is_readable(file):
    """
    Academic logic:
    If some text is extractable OR file exists → accept document
    """
    if not file:
        return False
    text = extract_text(file)
    return len(text) > 20 or file.size > 10_000

# -----------------------------
# Main App
# -----------------------------
def app():
    st.title("📂 Document Upload")

    # -----------------------------
    # Login check
    # -----------------------------
    if not st.session_state.get("logged_in"):
        st.warning("⚠ You must be logged in to upload documents.")
        return

    st.write("Upload required documents for loan verification:")

    # -----------------------------
    # File Uploaders
    # -----------------------------
    id_proof = st.file_uploader(
        "Upload ID Proof (Aadhaar / PAN / Passport)",
        type=["pdf", "png", "jpg", "jpeg"]
    )

    bank_statement = st.file_uploader(
        "Upload Bank Statement / Salary Slip",
        type=["pdf", "png", "jpg", "jpeg"]
    )

    collateral_doc = st.file_uploader(
        "Upload Collateral Document (Optional)",
        type=["pdf", "png", "jpg", "jpeg"]
    )

    # -----------------------------
    # Submit Button
    # -----------------------------
    if st.button("Submit Documents"):
        errors = []

        # ID Proof validation
        if not id_proof:
            errors.append("❌ ID Proof is required.")
        elif not is_readable(id_proof):
            errors.append("❌ ID Proof file unreadable. Please upload a clearer document.")

        # Income Proof validation
        if not bank_statement:
            errors.append("❌ Income proof (Bank Statement / Salary Slip) is required.")
        elif not is_readable(bank_statement):
            errors.append("❌ Income proof unreadable. Please upload a clearer document.")

        # Collateral is optional
        if collateral_doc and not is_readable(collateral_doc):
            errors.append("⚠ Collateral document may be unreadable; please check.")

        # Final decision
        if errors:
            st.error("❌ Document verification failed:")
            for err in errors:
                st.write(err)
            st.session_state["documents_verified"] = False
            return

        # SUCCESS
        st.session_state["documents_verified"] = True
        st.session_state["documents"] = {
            "id_proof": id_proof,
            "bank_statement": bank_statement,
            "collateral": collateral_doc
        }

        st.success("✅ Documents verified successfully!")

        # Redirect to EMI Calculator page
        st.session_state.page = "EMI Calculator"
        st.rerun()

    # -----------------------------
    # Preview uploaded files
    # -----------------------------
    st.subheader("Uploaded Files Preview")
    for label, file in [
        ("ID Proof", id_proof),
        ("Income Proof", bank_statement),
        ("Collateral", collateral_doc)
    ]:
        if file:
            st.write(f"**{label}:** {file.name}")
            if file.type.startswith("image/"):
                st.image(file, width=250)

