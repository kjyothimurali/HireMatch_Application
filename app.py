import streamlit as st

st.set_page_config(
    page_title="HireMatch",
    page_icon="💼",
    layout="wide"
)

st.title("💼 HireMatch")

st.markdown("""
# AI-Powered Job & Resume Analyzer

### Features

✅ Job Description Analysis

- Upload JD PDF
- Paste JD Text
- Predict Sector using BERT
- Predict Role using Cosine Similarity

---

✅ Resume Analysis

- Upload Resume PDF
- Select Sector
- Select Role
- Skill Gap Analysis
- Recommendations

---

✅ Dashboard

- View Previous Analyses
- Track Match Scores

Use the sidebar to navigate.
""")