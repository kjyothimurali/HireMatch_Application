import streamlit as st

from utils.pdf_reader import extract_pdf
from utils.skill_matcher import match_skills, suggest_improvements
from utils.history import save_history

# ─── Shared CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --bg: #0a0a0f;
    --surface: #111118;
    --border: #1e1e2e;
    --accent: #6c63ff;
    --accent2: #00e5a0;
    --danger: #ff6b6b;
    --warn: #ffd166;
    --text: #ffffff;
    --muted: #d1d5db;
    --card: #13131f;
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

.page-header {
    padding: 2.5rem 0 1rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 2rem;
}
.page-title {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin: 0;
    color: #ffffff;
}
.page-sub {
    color: #f3f4f6;
    font-size: 1rem;
    margin-top: 0.35rem;
    font-weight: 500;
}
/* File uploader */
[data-testid="stFileUploader"] {
    background: linear-gradient(
        135deg,
        #13131f,
        #18182a
    ) !important;

    border: 2px dashed #6c63ff !important;

    border-radius: 18px !important;

    padding: 2rem !important;

    box-shadow:
        0 0 20px rgba(108,99,255,0.15);

    transition: all 0.3s ease !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: #00e5a0 !important;

    box-shadow:
        0 0 30px rgba(0,229,160,0.2);
}

[data-testid="stFileUploader"] * {
    color: white !important;
}

[data-testid="stFileUploaderDropzone"] {
    background: transparent !important;
}

[data-testid="stFileUploaderDropzone"] * {
    color: white !important;
}
/* Selects */
.stSelectbox > div > div {
    background: #13131f !important;
    border: 1px solid #2c2c42 !important;
    border-radius: 12px !important;
    color: #ffffff !important;
}

/* Button */
.stButton > button {
    background: var(--accent) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    padding: 0.6rem 2rem !important;
    transition: opacity 0.2s, transform 0.15s !important;
}
.stButton > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}

/* Score gauge area */
.score-wrap {
    display: flex;
    align-items: center;
    gap: 2rem;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 2rem 2.5rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
    animation: fadeIn 0.4s ease;
}
.score-wrap::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
}
.score-circle {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    flex-shrink: 0;
    position: relative;
}
.score-meta { flex: 1; }
.score-meta-label {
    font-size: 0.72rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 0.3rem;
}
.score-meta-bar-bg {
    height: 8px;
    background: var(--border);
    border-radius: 100px;
    overflow: hidden;
    margin: 0.5rem 0;
}
.score-meta-bar-fill {
    height: 100%;
    border-radius: 100px;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
    transition: width 1.2s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Skills section */
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: var(--text);
    margin: 1.75rem 0 0.75rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.chips-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1rem;
}
.chip {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    border-radius: 100px;
    padding: 5px 14px;
    font-size: 0.78rem;
    font-weight: 500;
    animation: fadeIn 0.3s ease both;
}
.chip-match {
    background: rgba(0,229,160,0.1);
    border: 1px solid rgba(0,229,160,0.25);
    color: #00e5a0;
}
.chip-miss {
    background: rgba(255,107,107,0.1);
    border: 1px solid rgba(255,107,107,0.25);
    color: #ff8f8f;
}

/* Recommendation cards */
.rec-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    border-radius: 0 12px 12px 0;
    padding: 0.85rem 1.25rem;
    font-size: 0.95rem;
    color: #f8fafc;
    margin-bottom: 0.6rem;
    line-height: 1.6;
}
.rec-card strong { color: var(--text); }

.custom-warn {
    background: rgba(255,197,66,0.08);
    border: 1px solid rgba(255,197,66,0.25);
    border-radius: 10px;
    padding: 0.85rem 1.25rem;
    color: #ffd166;
    font-size: 0.875rem;
    margin-top: 1rem;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}
@keyframes slideIn {
    from { opacity: 0; transform: translateX(-8px); }
    to   { opacity: 1; transform: translateX(0); }
}
            /* ---------- GLOBAL TEXT FIX ---------- */

.block-container {
    max-width: 1200px !important;
}

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

.streamlit-expanderContent,
.streamlit-expanderHeader {
    color: #ffffff !important;
}

.stFileUploader label,
.stRadio label,
.stSelectbox label {
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Page Header ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <h1 class="page-title">📑 Resume Analysis</h1>
  <p class="page-sub">Upload your resume, select your target role, and get a detailed skill match report.</p>
</div>
""", unsafe_allow_html=True)

# ─── Inputs ───────────────────────────────────────────────────────────────────
col1, col2 = st.columns([1.2, 1])

with col1:
    resume = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"],
        label_visibility="visible"
    )

with col2:
    sector = st.selectbox(
        "Target Sector",
        ["IT", "Finance", "Healthcare", "Sales & Marketing"]
    )

    role_map = {
        "IT": ["Software Developer", "Web Developer", "Data Scientist", "ML Engineer"],
        "Finance": ["Accountant", "Financial Analyst", "Auditor"],
        "Healthcare": ["Doctor", "Nurse", "Medical Assistant"],
        "Sales & Marketing": ["Sales Executive", "Marketing Manager", "Business Analyst"]
    }

    role = st.selectbox("Target Role", role_map[sector])

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍  Analyze Resume"):

    if not resume:
        st.markdown('<div class="custom-warn">⚠️ Please upload a resume PDF to continue.</div>', unsafe_allow_html=True)

    else:
        with st.spinner("Extracting and matching skills…"):

            text = extract_pdf(resume)
            matched, missing = match_skills(text, sector)
            suggestions = suggest_improvements(missing)

            total = len(matched) + len(missing)
            score = int((len(matched) / total) * 100) if total > 0 else 0

            save_history("Resume Analysis", sector, role, score)

            # Score colors
            if score >= 70:
                score_color = "#00e5a0"
                score_label = "Strong Match"
            elif score >= 40:
                score_color = "#ffd166"
                score_label = "Partial Match"
            else:
                score_color = "#ff6b6b"
                score_label = "Needs Work"

            # ── Score card ──
            st.markdown(f"""
            <div class="score-wrap">
              <div class="score-circle" style="background: rgba(108,99,255,0.12); color: {score_color}; border: 2px solid {score_color}33;">
                {score}%
              </div>
              <div class="score-meta">
                <div class="score-meta-label">Resume Match Score — {sector} · {role}</div>
                <div style="font-family:'Syne',sans-serif; font-size:1.3rem; font-weight:700; color:{score_color};">
                  {score_label}
                </div>
                <div class="score-meta-bar-bg">
                  <div class="score-meta-bar-fill" style="width:{score}%;"></div>
                </div>
                <div style="font-size:0.8rem; color:var(--muted);">
                  {len(matched)} matched · {len(missing)} missing out of {total} skills evaluated
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

            # ── Matched Skills ──
            st.markdown('<div class="section-title">✅ Matched Skills</div>', unsafe_allow_html=True)
            if matched:
                chips_html = '<div class="chips-row">' + "".join(
                    f'<span class="chip chip-match">✓ {s}</span>' for s in matched
                ) + '</div>'
                st.markdown(chips_html, unsafe_allow_html=True)
            else:
                st.markdown('<p style="color:var(--muted); font-size:0.875rem;">No matching skills detected in the resume.</p>', unsafe_allow_html=True)

            # ── Missing Skills ──
            st.markdown('<div class="section-title">⛔ Missing Skills</div>', unsafe_allow_html=True)
            if missing:
                chips_html = '<div class="chips-row">' + "".join(
                    f'<span class="chip chip-miss">✗ {s}</span>' for s in missing
                ) + '</div>'
                st.markdown(chips_html, unsafe_allow_html=True)
            else:
                st.markdown('<p style="color:var(--accent2); font-size:0.875rem;">✓ All key skills are present!</p>', unsafe_allow_html=True)

            # ── Recommendations ──
            if suggestions:
                st.markdown('<div class="section-title">💡 Recommendations</div>', unsafe_allow_html=True)
                for item in suggestions:
                    st.markdown(f'<div class="rec-card">{item}</div>', unsafe_allow_html=True)
