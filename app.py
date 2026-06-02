import streamlit as st

st.set_page_config(
    page_title="Kori Pickle Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

TENNESSEE_ORANGE = "rgb(255, 130, 0)"
BLACK = "rgb(0, 0, 0)"
WARM_GRAY = "rgb(232, 227, 220)"
DARK_GRAY = "rgb(75, 75, 75)"
LINKEDIN_URL = "https://www.linkedin.com/in/kori-p-865jct"
GITHUB_URL = "https://github.com/koripickle1101-TN/priorauthiq-portfolio"
EMAIL_ADDRESS = "koripickle1101@gmail.com"

st.markdown(
    """
    <style>
    .stApp {
        background-color: rgb(255, 255, 255);
        color: rgb(0, 0, 0);
    }
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1180px;
    }
    h1, h2, h3 {
        letter-spacing: -0.02em;
    }
    .hero-title {
        font-family: Georgia, serif;
        font-size: 4.2rem;
        line-height: 1.0;
        color: rgb(0, 0, 0);
        margin-bottom: 0.25rem;
    }
    .hero-accent {
        color: rgb(255, 130, 0);
    }
    .subtitle {
        font-size: 1.15rem;
        color: rgb(75, 75, 75);
        margin-bottom: 1.25rem;
    }
    .section-title {
        font-family: Georgia, serif;
        font-size: 2rem;
        color: rgb(255, 130, 0);
        margin-top: 2.4rem;
        margin-bottom: 0.8rem;
    }
    .orange-rule {
        border: 0;
        height: 2px;
        background: linear-gradient(90deg, rgb(255, 130, 0), rgba(255, 130, 0, 0));
        margin: 1.8rem 0;
    }
    .card {
        border: 1px solid rgb(232, 227, 220);
        border-radius: 22px;
        padding: 1.35rem;
        min-height: 155px;
        background-color: rgb(255, 255, 255);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04);
    }
    .card-title {
        font-family: Georgia, serif;
        color: rgb(255, 130, 0);
        font-size: 1.3rem;
        margin-bottom: 0.5rem;
    }
    .node {
        width: 52px;
        height: 52px;
        border-radius: 50%;
        border: 2px solid rgb(255, 130, 0);
        box-shadow: 0 0 0 8px rgba(255, 130, 0, 0.09);
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        color: rgb(255, 130, 0);
        margin-bottom: 0.8rem;
    }
    .small-label {
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: rgb(75, 75, 75);
        font-size: 0.78rem;
        margin-bottom: 0.35rem;
    }
    .signature {
        font-family: Brush Script MT, Segoe Script, cursive;
        font-size: 2.3rem;
        color: rgb(40, 40, 40);
        transform: rotate(-1deg);
        margin-top: 0.1rem;
    }
    .footer {
        border-top: 1px solid rgb(232, 227, 220);
        margin-top: 3rem;
        padding-top: 1.5rem;
        text-align: center;
        color: rgb(75, 75, 75);
    }
    a {
        color: rgb(255, 130, 0);
        text-decoration: none;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("## Kori Pickle")
    st.write("BSHA Candidate")
    st.write("Healthcare Operations")
    st.write("Workflow Intelligence")
    st.write("Patient Experience to Operational Insight")
    st.markdown("---")
    st.write("Portfolio project")
    st.write("PriorAuthIQ")
    st.write("Status Active")
    st.markdown("---")
    st.markdown(f"[LinkedIn]({LINKEDIN_URL})")
    st.markdown(f"[Email](mailto:{EMAIL_ADDRESS})")
    st.markdown(f"[GitHub]({GITHUB_URL})")

st.markdown(
    """
    <div class="hero-title">Kori Pickle</div>
    <div class="subtitle">Healthcare Operations and Workflow Intelligence</div>
    <h3 class="hero-accent">Patient Experience to Operational Insight</h3>
    <hr class="orange-rule">
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='section-title'>Introduction</div>", unsafe_allow_html=True)
st.write("Hello and welcome.")
st.write("I am a Bachelor of Science in Healthcare Administration candidate focused on healthcare operations workflow intelligence patient access and revenue cycle performance.")
st.write("My professional interests were shaped by surviving a life threatening critical care event in 2014 and years of rehabilitation that followed.")
st.write("That experience taught me how operational decisions affect real patients.")
st.write("Today I study healthcare systems through the lens of workflow design communication operational efficiency and patient access.")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='card'><div class='node'>1</div><div class='card-title'>Current Status</div><p>BSHA Candidate<br>3.6 GPA<br>99 Completed Credits</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'><div class='node'>2</div><div class='card-title'>Professional Focus</div><p>Healthcare operations<br>Patient access<br>Revenue cycle performance</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='card'><div class='node'>3</div><div class='card-title'>Target Direction</div><p>Remote healthcare operations<br>Workflow improvement<br>Healthcare analytics</p></div>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>What Is PriorAuthIQ</div>", unsafe_allow_html=True)
st.write("PriorAuthIQ is a healthcare operations portfolio project that explores how organizations can reduce authorization delays improve operational visibility strengthen governance and better understand payer behavior.")
st.write("The platform was built to demonstrate healthcare systems thinking and operational analysis. It is a portfolio demonstration rather than a production healthcare software system.")

st.markdown("<div class='section-title'>Denial Risk Calculator</div>", unsafe_allow_html=True)
st.write("This interactive portfolio tool demonstrates how documentation readiness payer behavior and clinical urgency can be translated into a simple prior authorization risk score before submission.")
calc_left, calc_right = st.columns(2)
with calc_left:
    documentation = st.selectbox(
        "Documentation completeness",
        ["Complete", "Minor gaps", "Major gaps", "Missing required documentation"]
    )
    payer_volatility = st.selectbox(
        "Payer volatility",
        ["Low", "Moderate", "High", "Severe"]
    )
    clinical_urgency = st.selectbox(
        "Clinical urgency",
        ["Routine", "High", "Urgent", "Critical"]
    )
    service_line = st.selectbox(
        "Service line",
        ["Routine outpatient", "Advanced imaging", "Specialty pharmacy", "Surgery", "Cardiology", "Oncology"]
    )
with calc_right:
    missing_imaging = st.checkbox("Missing prerequisite imaging")
    missing_therapy = st.checkbox("Missing conservative therapy history")
    unsigned_order = st.checkbox("Unsigned physician order")
    payer_step_therapy = st.checkbox("Payer requires step therapy")

score = 0
score += {"Complete": 0, "Minor gaps": 10, "Major gaps": 25, "Missing required documentation": 40}[documentation]
score += {"Low": 0, "Moderate": 10, "High": 20, "Severe": 30}[payer_volatility]
score += {"Routine": 0, "High": 10, "Urgent": 20, "Critical": 30}[clinical_urgency]
score += {"Routine outpatient": 0, "Advanced imaging": 5, "Specialty pharmacy": 10, "Surgery": 15, "Cardiology": 20, "Oncology": 25}[service_line]
if missing_imaging:
    score += 20
if missing_therapy:
    score += 15
if unsigned_order:
    score += 5
if payer_step_therapy:
    score += 10
score = min(score, 100)

if score >= 75:
    risk_tier = "Severe Risk"
    recommended_action = "Do not submit yet. Route to clinical escalation or peer to peer preparation."
    owner = "Clinical Documentation Specialist and Physician Reviewer"
    patient_access_risk = "High"
    revenue_cycle_risk = "High"
elif score >= 40:
    risk_tier = "Elevated Risk"
    recommended_action = "Pend submission. Route to authorization specialist for manual chart review and addendum request."
    owner = "Authorization Specialist and Revenue Cycle Supervisor"
    patient_access_risk = "Moderate"
    revenue_cycle_risk = "Moderate"
else:
    risk_tier = "Low Risk"
    recommended_action = "Proceed with submission and continue routine status monitoring."
    owner = "Authorization Specialist"
    patient_access_risk = "Low"
    revenue_cycle_risk = "Low"

result_one, result_two, result_three = st.columns(3)
with result_one:
    st.metric("Risk Score", f"{score} out of 100")
with result_two:
    st.metric("Risk Tier", risk_tier)
with result_three:
    st.metric("Operational Owner", owner)

st.write("Recommended Action")
st.write(recommended_action)
st.write("Patient Access Risk")
st.write(patient_access_risk)
st.write("Revenue Cycle Risk")
st.write(revenue_cycle_risk)

st.markdown("<div class='section-title'>What This Project Demonstrates</div>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='card'><div class='card-title'>Workflow Intelligence</div><p>Analyzing intake documentation authorization routing escalation logic and downstream operational effects.</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'><div class='card-title'>Patient Access Focus</div><p>Connecting administrative delays to patient experience clinical access and timely care pathways.</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='card'><div class='card-title'>Revenue Cycle Awareness</div><p>Understanding how authorization delays denial risk and payer friction affect operational performance.</p></div>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>Platform Modules</div>", unsafe_allow_html=True)
modules = [
    "Prior Authorization Delay Reduction Framework",
    "Denial Prediction Engine",
    "Command Center Architecture",
    "Risk Scoring Playbook",
    "Executive Dashboard Guide",
    "Payer Intelligence Scorecard",
    "Escalation Governance Framework",
    "Executive Operations Playbook",
]
for module in modules:
    st.write(module)

st.markdown("<div class='section-title'>Why This Matters</div>", unsafe_allow_html=True)
st.write("I believe healthcare operations is most effective when administrative processes support rather than delay patient care.")
st.write("My goal is to contribute to healthcare organizations through thoughtful analysis structured problem solving and continuous operational improvement.")

st.markdown("<div class='section-title'>Contact</div>", unsafe_allow_html=True)
st.markdown(f"[LinkedIn]({LINKEDIN_URL})")
st.markdown(f"[Email](mailto:{EMAIL_ADDRESS})")
st.markdown(f"[GitHub Portfolio Repository]({GITHUB_URL})")

st.markdown(
    f"""
    <div class="footer">
        <div>Created by Kori Pickle</div>
        <div class="signature">Kori Pickle</div>
        <div><a href="{LINKEDIN_URL}">LinkedIn</a> &nbsp; <a href="{GITHUB_URL}">GitHub</a></div>
    </div>
    """,
    unsafe_allow_html=True,
)
