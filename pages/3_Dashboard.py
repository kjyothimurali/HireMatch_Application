import streamlit as st
import pandas as pd

from utils.history import load_history

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
            
/* KPI Cards */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin-bottom: 2rem;
}
.kpi-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.4rem 1.6rem;
    position: relative;
    overflow: hidden;
    animation: fadeUp 0.4s ease both;
}
.kpi-card::after {
    content: attr(data-icon);
    position: absolute;
    right: 1rem;
    top: 1rem;
    font-size: 1.4rem;
    opacity: 0.35;
}
.kpi-label {
    font-size: 0.75rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #d1d5db;
    margin-bottom: 0.4rem;
    font-weight: 700;
}
.kpi-value {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #ffffff;
    line-height: 1;
}
.kpi-sub {
    font-size: 0.85rem;
    color: #cbd5e1;
    margin-top: 0.35rem;
}

/* Chart sections */
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: #ffffff;
    margin: 2rem 0 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--border);
}

/* Dataframe */
.stDataFrame {
    border-radius: 12px !important;
    overflow: hidden !important;
    border: 1px solid var(--border) !important;
}
[data-testid="stDataFrame"] {
    border-radius: 12px !important;
    overflow: hidden !important;
}

[data-testid="stDataFrame"] table {
    color: white !important;
}

[data-testid="stDataFrame"] th {
    background: #1f2937 !important;
    color: white !important;
}

[data-testid="stDataFrame"] td {
    color: white !important;
}

/* Chart containers */
.element-container .stBarChart canvas {
    background: transparent !important;
}

/* Empty state */
.empty-state {
    text-align: center;
    padding: 5rem 2rem;
    color: #d1d5db;
}

.empty-state-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 0.5rem;
}

.empty-state-sub {
    font-size: 0.95rem;
    line-height: 1.65;
    color: #e5e7eb;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}

@media (max-width: 800px) {
    .kpi-grid { grid-template-columns: repeat(2, 1fr); }
}
            /* ---------- GLOBAL TEXT FIX ---------- */

.block-container {
    max-width: 1300px !important;
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

/* DataFrame readability */

[data-testid="stDataFrame"] * {
    color: #ffffff !important;
}

[data-testid="stDataFrame"] th {
    background: #1f2937 !important;
    color: white !important;
}

[data-testid="stDataFrame"] td {
    background: #13131f !important;
    color: white !important;
}

/* Tabs */

button[data-baseweb="tab"] {
    color: white !important;
    font-weight: 600 !important;
}

/* Sidebar */

[data-testid="stSidebar"] * {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ─── Page Header ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <h1 class="page-title">📊 Dashboard</h1>
  <p class="page-sub">Track your analysis history, match scores, and sector insights.</p>
</div>
""", unsafe_allow_html=True)

df = load_history()

if df.empty:
    st.markdown("""
    <div class="empty-state">
      <span class="empty-state-icon">📭</span>
      <div class="empty-state-title">No analyses yet</div>
      <div class="empty-state-sub">
        Run a Job Analysis or Resume Analysis to see your results here.
      </div>
    </div>
    """, unsafe_allow_html=True)

else:
    # ── KPI Cards ──────────────────────────────────────────────────────────────
    total_analyses = len(df)
    avg_score      = round(df["Score"].mean(), 1)
    top_sector     = df["Sector"].value_counts().idxmax() if not df.empty else "—"
    job_count      = len(df[df["Type"] == "Job Analysis"])
    resume_count   = len(df[df["Type"] == "Resume Analysis"])

    st.markdown(f"""
    <div class="kpi-grid">

      <div class="kpi-card" data-icon="🔍">
        <div class="kpi-label">Total Analyses</div>
        <div class="kpi-value">{total_analyses}</div>
        <div class="kpi-sub">{job_count} job · {resume_count} resume</div>
      </div>

      <div class="kpi-card" data-icon="📈">
        <div class="kpi-label">Avg Match Score</div>
        <div class="kpi-value">{avg_score}%</div>
        <div class="kpi-sub">Across all analyses</div>
      </div>

      <div class="kpi-card" data-icon="🏢">
        <div class="kpi-label">Top Sector</div>
        <div class="kpi-value" style="font-size:1.3rem;">{top_sector}</div>
        <div class="kpi-sub">Most analyzed</div>
      </div>

      <div class="kpi-card" data-icon="✅">
        <div class="kpi-label">High Matches (≥70%)</div>
        <div class="kpi-value">{len(df[df['Score'] >= 70])}</div>
        <div class="kpi-sub">Strong result count</div>
      </div>

    </div>
    """, unsafe_allow_html=True)

    # ── Tabs ───────────────────────────────────────────────────────────────────
    tab1, tab2, tab3 = st.tabs(["📋 History", "📊 Score Distribution", "🏢 Sector Breakdown"])

    with tab1:
        st.markdown('<div class="section-title">All Analyses</div>', unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)

    with tab2:
        st.markdown('<div class="section-title">Match Score per Analysis</div>', unsafe_allow_html=True)
        chart_df = pd.DataFrame({"Score": df["Score"].values})
        st.bar_chart(chart_df, color="#6c63ff")

    with tab3:
        st.markdown('<div class="section-title">Analyses by Sector</div>', unsafe_allow_html=True)
        sector_counts = df["Sector"].value_counts()
        st.bar_chart(sector_counts, color="#00e5a0")
