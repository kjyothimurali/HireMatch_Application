import streamlit as st

st.set_page_config(
    page_title="HireMatch",
    page_icon="💼",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --bg: #0a0a0f;
    --surface: #111118;
    --border: #1e1e2e;
    --accent: #6c63ff;
    --accent2: #00e5a0;
    --accent3: #ff6b6b;
    --text: #e8e8f0;
    --muted: #6b6b80;
    --card: #13131f;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}

.stApp {
    background: var(--bg) !important;
}

#MainMenu, footer, header { visibility: hidden; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] * {
    color: var(--text) !important;
}

/* Hero */
.hero-wrap {
    min-height: 90vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
    padding: 4rem 2rem;
}

.hero-bg {
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 80% 60% at 50% -10%, rgba(108,99,255,0.22) 0%, transparent 70%),
                radial-gradient(ellipse 60% 40% at 80% 80%, rgba(0,229,160,0.10) 0%, transparent 60%);
    pointer-events: none;
}

.noise-overlay {
    position: absolute;
    inset: 0;
    opacity: 0.03;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

.badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(108,99,255,0.12);
    border: 1px solid rgba(108,99,255,0.3);
    color: #a09aff;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 6px 14px;
    border-radius: 100px;
    margin-bottom: 2rem;
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(3rem, 7vw, 6rem);
    font-weight: 800;
    line-height: 1.05;
    text-align: center;
    letter-spacing: -0.03em;
    margin-bottom: 1.5rem;
    background: linear-gradient(135deg, #e8e8f0 30%, #a09aff 70%, #00e5a0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-sub {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.15rem;
    color: var(--muted);
    text-align: center;
    max-width: 560px;
    line-height: 1.7;
    margin-bottom: 3rem;
    font-weight: 300;
}

.cta-row {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 5rem;
}

.cta-primary {
    background: var(--accent);
    color: white;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 0.95rem;
    padding: 12px 28px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    transition: opacity 0.2s, transform 0.2s;
}

.cta-secondary {
    background: transparent;
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 0.95rem;
    padding: 12px 28px;
    border-radius: 10px;
    border: 1px solid var(--border);
    cursor: pointer;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

/* Feature Grid */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.25rem;
    width: 100%;
    max-width: 1100px;
    margin: 0 auto;
    padding: 0 1rem;
}

.feat-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 2rem;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s, transform 0.2s;
}

.feat-card:hover {
    border-color: rgba(108,99,255,0.4);
    transform: translateY(-2px);
}

.feat-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 80% 60% at 50% -30%, rgba(108,99,255,0.08), transparent 70%);
    pointer-events: none;
}

.feat-icon {
    font-size: 1.8rem;
    margin-bottom: 1rem;
    display: block;
}

.feat-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 0.5rem;
}

.feat-desc {
    font-size: 0.875rem;
    color: var(--muted);
    line-height: 1.65;
}

.feat-tag {
    display: inline-block;
    margin-top: 1rem;
    font-size: 0.7rem;
    font-weight: 500;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    padding: 3px 10px;
    border-radius: 100px;
}

.tag-purple { background: rgba(108,99,255,0.15); color: #a09aff; }
.tag-green  { background: rgba(0,229,160,0.12); color: #00e5a0; }
.tag-red    { background: rgba(255,107,107,0.12); color: #ff8f8f; }

/* Stats strip */
.stats-strip {
    display: flex;
    gap: 2rem;
    flex-wrap: wrap;
    justify-content: center;
    margin: 4rem auto 0;
    padding: 2rem;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    max-width: 800px;
}

.stat-item {
    text-align: center;
}

.stat-num {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: var(--text);
    display: block;
}

.stat-label {
    font-size: 0.8rem;
    color: var(--muted);
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* Divider */
.section-divider {
    width: 100%;
    height: 1px;
    background: var(--border);
    margin: 3rem 0;
}
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero-wrap">
  <div class="hero-bg"></div>
  <div class="noise-overlay"></div>

  <span class="badge">✦ AI-Powered Hiring Intelligence</span>

  <h1 class="hero-title">Match Smarter.<br/>Hire Better.</h1>

  <p class="hero-sub">
    HireMatch uses BERT and semantic similarity to decode job descriptions, 
    score resumes, and surface the skill gaps that matter — instantly.
  </p>

  <div class="cta-row">
    <a class="cta-primary" href="/Job_Analysis">⚡ Analyze a Job</a>
    <a class="cta-secondary" href="/Resume_Analysis">📑 Score My Resume</a>
  </div>

</div>
""", unsafe_allow_html=True)

# Features
st.markdown("""
<div class="feature-grid">

  <div class="feat-card">
    <span class="feat-icon">🧠</span>
    <div class="feat-title">BERT Sector Classification</div>
    <div class="feat-desc">Fine-tuned BERT model classifies job descriptions into Finance, Healthcare, IT, or Sales & Marketing with confidence scoring.</div>
    <span class="feat-tag tag-purple">Deep Learning</span>
  </div>

  <div class="feat-card">
    <span class="feat-icon">🎯</span>
    <div class="feat-title">Role Prediction via TF-IDF</div>
    <div class="feat-desc">Cosine similarity across a curated dataset surfaces the most relevant role title for any job description in milliseconds.</div>
    <span class="feat-tag tag-green">NLP Matching</span>
  </div>

  <div class="feat-card">
    <span class="feat-icon">📊</span>
    <div class="feat-title">Skill Gap Analysis</div>
    <div class="feat-desc">Upload your resume, get an instant match score, see exactly which skills are missing, and receive actionable recommendations.</div>
    <span class="feat-tag tag-red">Resume Intel</span>
  </div>

  <div class="feat-card">
    <span class="feat-icon">📈</span>
    <div class="feat-title">Analytics Dashboard</div>
    <div class="feat-desc">Track every analysis, monitor match scores over time, and visualize sector distribution across your history.</div>
    <span class="feat-tag tag-purple">Insights</span>
  </div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="stats-strip">
  <div class="stat-item">
    <span class="stat-num">4</span>
    <span class="stat-label">Sectors</span>
  </div>
  <div class="stat-item">
    <span class="stat-num">BERT</span>
    <span class="stat-label">Sector Model</span>
  </div>
  <div class="stat-item">
    <span class="stat-num">TF-IDF</span>
    <span class="stat-label">Role Matching</span>
  </div>
  <div class="stat-item">
    <span class="stat-num">PDF</span>
    <span class="stat-label">JD & Resume</span>
  </div>
</div>
""", unsafe_allow_html=True)
