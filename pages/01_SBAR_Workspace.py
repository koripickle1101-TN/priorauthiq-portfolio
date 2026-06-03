import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="SBAR Workspace", page_icon="🟠", layout="wide")

TENNESSEE_ORANGE = "#FF8200"
BLACK = "#000000"
WARM_GRAY = "#E8E3DC"

st.markdown("""
<style>
.stApp { background-color: #FFFFFF; color: #000000; }
.main .block-container { max-width: 1180px; padding-top: 2.5rem; padding-bottom: 3rem; }
h1, h2, h3 { font-family: Georgia, serif; letter-spacing: -0.03em; }
.kori-hero { border-bottom: 2px solid #FF8200; padding-bottom: 1.4rem; margin-bottom: 2rem; }
.kori-signature { font-family: Brush Script MT, Segoe Script, cursive; font-size: 3.2rem; color: #000000; line-height: 1; }
.kori-kicker { color: #FF8200; text-transform: uppercase; letter-spacing: .22em; font-size: .78rem; font-weight: 800; }
.kori-title { font-family: Georgia, serif; font-size: 3.4rem; line-height: 1; color: #000000; margin-top: .25rem; }
.orange { color: #FF8200; }
.card { border: 1px solid #E8E3DC; background: #FFFFFF; padding: 1.2rem; border-radius: 18px; box-shadow: 0 10px 30px rgba(0,0,0,.04); min-height: 145px; }
.node { width: 46px; height: 46px; border-radius: 50%; border: 3px solid #FF8200; box-shadow: 0 0 0 8px rgba(255,130,0,.08); display: flex; align-items:center; justify-content:center; color:#FF8200; font-weight:800; margin-bottom:.7rem; }
.footer { border-top: 1px solid #E8E3DC; margin-top: 3rem; padding-top: 1.5rem; text-align: center; color: #555; }
.footer-signature { font-family: Brush Script MT, Segoe Script, cursive; font-size: 2.7rem; color: #111; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='kori-hero'>
  <div class='kori-signature'>Kori Pickle</div>
  <div class='kori-kicker'>Healthcare Operations Intelligence</div>
  <div class='kori-title'>SBAR Clinical Safety <span class='orange'>Workspace</span></div>
</div>
""", unsafe_allow_html=True)

st.write("Use this workspace to practice clear SBAR communication. The goal is to organize the immediate problem, the relevant background, the assessment, and the specific recommendation without creating confusion or delay.")

st.markdown("### Scenario Simulator")
scenario = st.selectbox(
    "Choose a practice scenario",
    [
        "Blank SBAR workspace",
        "Acute heart failure escalation",
        "Emerging sepsis escalation",
        "Patient access scheduling breakdown",
    ],
)

scenario_data = {
    "Blank SBAR workspace": {
        "name": "", "unit": "", "patient": "", "baseline": "", "s": "", "b": "", "a": "", "r": ""
    },
    "Acute heart failure escalation": {
        "name": "Sharon Taylor RN",
        "unit": "Cardiac Care Unit",
        "patient": "Mr. Arthur Pendelton Room 304",
        "baseline": "Acute exacerbation of heart failure",
        "s": "The patient has developed sudden respiratory distress with oxygen saturation dropping to 86 percent on 2 liters by nasal cannula.",
        "b": "The patient was admitted 48 hours ago for heart failure exacerbation. Current vital signs show blood pressure 168 over 94, heart rate 112, respiratory rate 28, and coarse crackles bilaterally. The morning diuretic dose was held due to borderline potassium.",
        "a": "I am concerned about acute pulmonary edema and worsening fluid overload with respiratory decompensation.",
        "r": "I need an immediate bedside evaluation, oxygen escalation, and orders for appropriate diuretic management or additional respiratory support.",
    },
    "Emerging sepsis escalation": {
        "name": "Marcus Vance BSN",
        "unit": "Medical Surgical Floor",
        "patient": "Mrs. Eleanor Vance Room 412B",
        "baseline": "Post operative partial colectomy",
        "s": "The patient is showing signs of possible sepsis with fever, hypotension, tachycardia, and new confusion.",
        "b": "The patient is post operative day 2. Temperature is 38.9 Celsius, blood pressure dropped to 94 over 52, heart rate is 122, respiratory rate is 24, and white blood cell count is 18500.",
        "a": "I am concerned about emerging sepsis or septic shock and possible post operative infection.",
        "r": "I need urgent provider evaluation, sepsis protocol review, lactic acid, blood cultures, fluid bolus consideration, and antibiotic evaluation.",
    },
    "Patient access scheduling breakdown": {
        "name": "Kori Pickle",
        "unit": "Outpatient Specialty Clinic",
        "patient": "Patient access scheduling queue",
        "baseline": "Scheduling error with high travel burden",
        "s": "A patient arrived for an appointment today, but the system shows the visit was entered for tomorrow.",
        "b": "The patient traveled over 60 miles using paid transportation. The physician schedule is full, but an emergency hold slot is open and another provider has availability in 20 minutes.",
        "a": "This is an operational access failure that could create patient dissatisfaction, delay care, and increase unnecessary burden.",
        "r": "I recommend using the emergency hold slot or transferring the patient into the available provider slot today to prevent a failed visit.",
    },
}

data = scenario_data[scenario]

st.markdown("### Required Pre Communication Checks")
check1 = st.checkbox("I can clearly explain why this issue matters now.")
check2 = st.checkbox("I have the relevant chart, notes, data, or scenario details available.")
check3 = st.checkbox("I know the specific action I need from the receiver.")
ready = check1 and check2 and check3

if not ready:
    st.warning("Complete all three checks to unlock the SBAR builder.")

left, right = st.columns([1, 1])
with left:
    st.markdown("### SBAR Inputs")
    name = st.text_input("Clinician or communicator name", value=data["name"], disabled=not ready)
    unit = st.text_input("Department or setting", value=data["unit"], disabled=not ready)
    patient = st.text_input("Patient or case location", value=data["patient"], disabled=not ready)
    baseline = st.text_input("Baseline issue", value=data["baseline"], disabled=not ready)
    situation = st.text_area("S Situation", value=data["s"], height=120, disabled=not ready)
    background = st.text_area("B Background", value=data["b"], height=150, disabled=not ready)
    assessment = st.text_area("A Assessment", value=data["a"], height=120, disabled=not ready)
    recommendation = st.text_area("R Recommendation", value=data["r"], height=120, disabled=not ready)

with right:
    st.markdown("### Dynamic SBAR Script")
    script = f"""SBAR COMMUNICATION SCRIPT

Opening
Hello, this is {name or '[Name]'} calling from {unit or '[Department or Setting]'} about {patient or '[Patient or Case Location]'}.

Situation
The immediate issue is:
{situation or '[Add the immediate problem here.]'}

Background
The relevant background is:
{background or '[Add the relevant context here.]'}

Assessment
My assessment of the concern is:
{assessment or '[Add what the information appears to mean.]'}

Recommendation
My requested next action is:
{recommendation or '[Add the specific action needed next.]'}

Baseline Issue
The baseline issue or case context is:
{baseline or '[Add diagnosis, workflow issue, or case background.]'}

Close The Loop
Please repeat back any orders, next steps, timing expectations, or escalation instructions so the plan is clear.

Created by Kori Pickle
Healthcare Operations Intelligence
"""
    st.text_area("Copy ready script", script, height=520)

st.markdown("### Response Timer")
if "timer_start" not in st.session_state:
    st.session_state.timer_start = None

col_a, col_b = st.columns(2)
with col_a:
    if st.button("Start 5 Minute Timer", disabled=not ready):
        st.session_state.timer_start = datetime.now()
with col_b:
    if st.button("Reset Timer"):
        st.session_state.timer_start = None

if st.session_state.timer_start:
    elapsed = datetime.now() - st.session_state.timer_start
    remaining = max(timedelta(minutes=5) - elapsed, timedelta(seconds=0))
    st.metric("Timer Remaining", str(remaining).split('.')[0])
    if remaining.total_seconds() == 0:
        st.error("Timer complete. In a real setting, follow the appropriate escalation pathway or chain of command.")

st.markdown("### What This Demonstrates")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("<div class='card'><div class='node'>S</div><b>Situation</b><br>Immediate problem clarity.</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'><div class='node'>B</div><b>Background</b><br>Relevant context without overload.</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='card'><div class='node'>A</div><b>Assessment</b><br>Risk framing and interpretation.</div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='card'><div class='node'>R</div><b>Recommendation</b><br>Specific action request.</div>", unsafe_allow_html=True)

st.markdown("""
<div class='footer'>
  <div>Created by Kori Pickle</div>
  <div class='footer-signature'>Kori Pickle</div>
  <div>LinkedIn · GitHub</div>
</div>
""", unsafe_allow_html=True)
