import streamlit as st

from utils.predictor import predict_sector
from utils.role_predictor import predict_role
from utils.pdf_reader import extract_pdf
from utils.history import save_history

# ─── Shared CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --bg: #0a0a0f;
    --surface: #111118;
    --border: #2c2c42;

    --accent: #6c63ff;
    --accent2: #00e5a0;

    --text: #ffffff;
    --muted: #d1d5db;

    --card: #13131f;
    --danger: #ff6b6b;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}

.stApp { background: var(--bg) !important; }
#MainMenu, footer, header { visibility: hidden; }

[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text) !important; }

/* Page header */
.page-header {
    padding: 2.5rem 0 1rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 2rem;
}
.page-title {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    color: #ffffff !important;
    letter-spacing: -0.02em;
    margin: 0;
}
.page-sub {
    color: #f3f4f6 !important;
    font-size: 1rem;
    margin-top: 0.35rem;
    font-weight: 500;
}

/* Tab-like radio */
div[data-baseweb="radio"] > div {
    display: flex !important;
    flex-direction: row !important;
    gap: 0.75rem !important;
    flex-wrap: wrap;
}
div[data-baseweb="radio"] label {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    padding: 10px 20px !important;
    color: #ffffff !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    transition: all 0.2s !important;
}
div[data-baseweb="radio"] label:has(input:checked) {
    border-color: var(--accent) !important;
    color: #a09aff !important;
    background: rgba(108,99,255,0.1) !important;
}

/* Upload zone */
[data-testid="stFileUploader"] {
    background: #13131f !important;
    border: 2px dashed #6c63ff !important;
    border-radius: 16px !important;
    padding: 1.5rem !important;
}

[data-testid="stFileUploader"] * {
    color: white !important;
}

[data-testid="stFileUploader"] button {
    background: #6c63ff !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
}

[data-testid="stFileUploader"] section {
    background: transparent !important;
}

[data-testid="stFileUploader"] small {
    color: #d1d5db !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: var(--accent) !important;
}

/* Text area */
.stTextArea textarea {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: #ffffff !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1rem !important;
}

.stTextArea textarea::placeholder {
    color: #cbd5e1 !important;
    opacity: 1 !important;
}
.stTextArea textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(108,99,255,0.15) !important;
}

/* Button */
.stButton > button {
    background: var(--accent) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    padding: 0.6rem 2rem !important;
    transition: opacity 0.2s, transform 0.15s !important;
    width: auto !important;
}
.stButton > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}

/* Result cards */
.result-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.25rem;
    margin-top: 1.5rem;
}
.result-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.75rem;
    position: relative;
    overflow: hidden;
    animation: slideUp 0.4s ease both;
}
.result-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    border-radius: 2px 2px 0 0;
}
.card-purple::before { background: linear-gradient(90deg, var(--accent), #a09aff); }
.card-green::before  { background: linear-gradient(90deg, var(--accent2), #00c87a); }

.result-label {
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #e5e7eb !important;
    margin-bottom: 0.4rem;
}
.result-value {
    font-family: 'Syne', sans-serif;
    font-size: 1.8rem;
    font-weight: 700;
    color: #ffffff !important;
    margin-bottom: 0.75rem;
}
.conf-bar-bg {
    height: 6px;
    background: var(--border);
    border-radius: 100px;
    overflow: hidden;
}
.conf-bar-fill {
    height: 100%;
    border-radius: 100px;
    transition: width 1s cubic-bezier(0.4, 0, 0.2, 1);
}
.conf-pct {
    font-size: 0.95rem;
    color: #ffffff !important;
    margin-top: 0.4rem;
    font-weight: 600;
}

/* Spinner */
.stSpinner > div {
    border-color: var(--accent) transparent transparent transparent !important;
}

/* Expander */
.streamlit-expanderHeader {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-family: 'DM Sans', sans-serif !important;
}
.streamlit-expanderContent {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-top: none !important;
    border-radius: 0 0 10px 10px !important;
    color: var(--muted) !important;
    font-size: 0.85rem !important;
}

/* Alert box */
.custom-alert {
    background: rgba(255,107,107,0.08);
    border: 1px solid rgba(255,107,107,0.25);
    border-radius: 10px;
    padding: 0.85rem 1.25rem;
    color: #ff8f8f;
    font-size: 0.875rem;
    margin-top: 1rem;
}
.custom-warn {
    background: rgba(255,197,66,0.08);
    border: 1px solid rgba(255,197,66,0.25);
    border-radius: 10px;
    padding: 0.85rem 1.25rem;
    color: #ffd166;
    font-size: 0.875rem;
    margin-top: 1rem;
}

@keyframes slideUp {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}

@media (max-width: 640px) {
    .result-grid { grid-template-columns: 1fr; }
}
            /* ---------- GLOBAL VISIBILITY FIX ---------- */

p,
span,
label,
div,
small,
li {
    color: #f8fafc !important;
}

h1,
h2,
h3,
h4,
h5,
h6 {
    color: #ffffff !important;
}

[data-testid="stMarkdownContainer"] {
    color: #ffffff !important;
}

.streamlit-expanderContent {
    color: #ffffff !important;
}

.streamlit-expanderHeader {
    color: #ffffff !important;
}

.stFileUploader label {
    color: #ffffff !important;
}

.stRadio label {
    color: #ffffff !important;
}

.stSelectbox label {
    color: #ffffff !important;
}
            /* Fix upload text visibility */

[data-testid="stFileUploaderDropzone"] {
    background: #13131f !important;
}

[data-testid="stFileUploaderDropzone"] * {
    color: white !important;
}

[data-testid="stFileUploaderDropzoneInstructions"] {
    color: white !important;
}

[data-testid="stFileUploaderDropzone"] button {
    background: #6c63ff !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Page Header ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <h1 class="page-title">📄 Job Analysis</h1>
  <p class="page-sub">Predict the sector and role from any job description using BERT + cosine similarity.</p>
</div>
""", unsafe_allow_html=True)

# ─── Input Method ─────────────────────────────────────────────────────────────
input_method = st.radio(
    "Input Method",
    ["✏️  Paste JD", "📎  Upload PDF"],
    label_visibility="collapsed",
    horizontal=True
)

text = ""

if "Paste" in input_method:
    text = st.text_area(
        "Paste Job Description",
        placeholder="Paste the full job description here…",
        height=280,
        label_visibility="collapsed"
    )
else:
    uploaded_file = st.file_uploader(
        "Upload JD PDF",
        type=["pdf"],
        label_visibility="collapsed"
    )
    if uploaded_file:
        text = extract_pdf(uploaded_file)
        st.markdown(f"""
        <div style="font-size:0.8rem; color: var(--accent2); margin-top:0.5rem;">
            ✓ Extracted {len(text.split())} words from PDF
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("⚡  Analyze Job Description"):

    if not text.strip():
        st.markdown('<div class="custom-warn">⚠️ Please provide a job description to analyze.</div>', unsafe_allow_html=True)

    else:
        with st.spinner("Running BERT classification & role matching…"):

            sector, confidence = predict_sector(text)

            if sector == "Other / Unknown":
                st.markdown(f"""
                <div class="custom-alert">
                    ✗ Sector could not be determined (confidence: {confidence*100:.1f}%). 
                    Try a more detailed job description.
                </div>
                """, unsafe_allow_html=True)

            else:
                role, similarity = predict_role(text, sector)

                save_history(
                    "Job Analysis",
                    sector,
                    role,
                    round(similarity * 100, 2)
                )

                conf_pct = round(confidence * 100, 1)
                sim_pct  = round(similarity  * 100, 1)

                # Color for bars
                conf_color = "#6c63ff"
                sim_color  = "#00e5a0"

                st.markdown(f"""
                <div class="result-grid">

                  <div class="result-card card-purple">
                    <div class="result-label">Predicted Sector</div>
                    <div class="result-value">{sector}</div>
                    <div class="conf-bar-bg">
                      <div class="conf-bar-fill" style="width:{conf_pct}%; background:{conf_color};"></div>
                    </div>
                    <div class="conf-pct">Confidence: <strong style="color:var(--text)">{conf_pct}%</strong></div>
                  </div>

                  <div class="result-card card-green">
                    <div class="result-label">Best Matching Role</div>
                    <div class="result-value">{role}</div>
                    <div class="conf-bar-bg">
                      <div class="conf-bar-fill" style="width:{sim_pct}%; background:{sim_color};"></div>
                    </div>
                    <div class="conf-pct">Similarity: <strong style="color:var(--text)">{sim_pct}%</strong></div>
                  </div>

                </div>
                """, unsafe_allow_html=True)

                with st.expander("🔍 View Extracted Text"):
                    st.write(text[:5000])
