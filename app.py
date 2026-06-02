import streamlit as st

st.set_page_config(
    page_title="Kori Pickle Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

TENNESSEE_ORANGE = "rgb(255, 130, 0)"
BLACK = "rgb(0, 0, 0)"
WARM_GRAY = "rgb(232, 227, 220)"
DARK_GRAY = "rgb(75, 75, 75)"

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
    st.markdown("<div class='card'><div class='node'>1</div><div class='card-title'>Current Status</div><p>BSHA Candidate<br>Three Point Six GPA<br>Ninety Nine Completed Credits</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'><div class='node'>2</div><div class='card-title'>Professional Focus</div><p>Healthcare operations<br>Patient access<br>Revenue cycle performance</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='card'><div class='node'>3</div><div class='card-title'>Target Direction</div><p>Remote healthcare operations<br>Workflow improvement<br>Healthcare analytics</p></div>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>What Is PriorAuthIQ</div>", unsafe_allow_html=True)
st.write("PriorAuthIQ is a healthcare operations portfolio project that explores how organizations can reduce authorization delays improve operational visibility strengthen governance and better understand payer behavior.")
st.write("The platform was built to demonstrate healthcare systems thinking and operational analysis. It is a portfolio demonstration rather than a production healthcare software system.")

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
st.write("LinkedIn")
st.write("Email")
st.write("GitHub")

st.markdown(
    """
    <div class="footer">
        <div>Created by Kori Pickle</div>
        <div class="signature">Kori Pickle</div>
        <div>LinkedIn  GitHub</div>
    </div>
    """,
    unsafe_allow_html=True,
)
