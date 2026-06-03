import streamlit as st

st.set_page_config(page_title="Healthcare Operations Study Lab", page_icon="🟠", layout="wide")

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
.card { border: 1px solid #E8E3DC; background: #FFFFFF; padding: 1.2rem; border-radius: 18px; box-shadow: 0 10px 30px rgba(0,0,0,.04); min-height: 150px; }
.node { width: 46px; height: 46px; border-radius: 50%; border: 3px solid #FF8200; box-shadow: 0 0 0 8px rgba(255,130,0,.08); display: flex; align-items:center; justify-content:center; color:#FF8200; font-weight:800; margin-bottom:.7rem; }
.footer { border-top: 1px solid #E8E3DC; margin-top: 3rem; padding-top: 1.5rem; text-align: center; color: #555; }
.footer-signature { font-family: Brush Script MT, Segoe Script, cursive; font-size: 2.7rem; color: #111; }
</style>
""", unsafe_allow_html=True)

if "flash_index" not in st.session_state:
    st.session_state.flash_index = 0
if "show_answer" not in st.session_state:
    st.session_state.show_answer = False
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

flashcards = [
    ("What does probability sampling mean?", "Probability sampling means every eligible person in the population has a known chance of being selected. This reduces bias and makes the findings more trustworthy."),
    ("What does nonprobability sampling mean?", "Nonprobability sampling means participants are selected based on convenience, availability, judgment, or specific characteristics. It can be useful, but it may not represent the full population as strongly."),
    ("Why would stratified random sampling work for an EMR effectiveness study?", "Stratified random sampling works because different staff groups experience the EMR differently. Nurses, providers, patient access staff, billing staff, and health information staff may each see different workflow problems."),
    ("What is one survey use for an EMR study?", "A survey could collect staff feedback about EMR usability, documentation burden, communication problems, duplicate work, missing fields, and workflow barriers."),
    ("Why use interviews or focus groups?", "Interviews and focus groups help explain why problems are happening. Surveys can show what is happening, but interviews reveal workflow breakdowns and communication gaps in more detail."),
    ("What objective EMR data could be reviewed?", "Useful EMR report data could include documentation completion time, missing fields, error rates, duplicate entries, message delays, turnaround time, and incomplete records."),
    ("How does EMR effectiveness connect to healthcare operations?", "EMR effectiveness connects to workflow design, documentation quality, communication, patient access, care coordination, staff efficiency, and revenue cycle performance."),
    ("What does denial prevention mean from an operations perspective?", "Denial prevention means identifying risk before submission by improving documentation readiness, payer requirement awareness, authorization workflows, and handoffs."),
    ("What does operational visibility mean?", "Operational visibility means making work visible through dashboards, queues, reports, escalation triggers, and performance signals so leaders can act before problems grow."),
]

quiz = [
    {"q": "Which sampling method gives every eligible person a known chance of being selected?", "options": ["Convenience sampling", "Probability sampling", "Judgment sampling", "Snowball sampling"], "answer": "Probability sampling"},
    {"q": "Which method best shows differences between nurses providers billing staff and patient access staff?", "options": ["Stratified random sampling", "Only interviewing one manager", "Using only volunteers", "Ignoring staff role"], "answer": "Stratified random sampling"},
    {"q": "Which data collection method gives measurable system evidence?", "options": ["Focus group opinions", "EMR system reports", "Informal hallway conversations", "Guessing from complaints"], "answer": "EMR system reports"},
    {"q": "Why can nonprobability sampling be weaker?", "options": ["It always uses too many people", "It never collects data", "Not everyone has an equal chance of being selected", "It only works for finance"], "answer": "Not everyone has an equal chance of being selected"},
    {"q": "What is the strongest healthcare operations angle for EMR effectiveness?", "options": ["Whether screen colors look nice", "Workflow documentation communication access and staff efficiency", "Only whether one person likes it", "Ignoring departments"], "answer": "Workflow documentation communication access and staff efficiency"},
]

st.markdown("""
<div class='kori-hero'>
  <div class='kori-signature'>Kori Pickle</div>
  <div class='kori-kicker'>Healthcare Operations Intelligence</div>
  <div class='kori-title'>Daily Healthcare Operations <span class='orange'>Study Lab</span></div>
</div>
""", unsafe_allow_html=True)

st.write("Use this page daily to study HCS 465 research concepts and connect them to healthcare operations, patient access, denial prevention, workflow intelligence, and portfolio language.")

st.markdown("### Daily Study Checklist")
col1, col2, col3, col4 = st.columns(4)
with col1:
    c1 = st.checkbox("Review flashcards")
with col2:
    c2 = st.checkbox("Complete quiz")
with col3:
    c3 = st.checkbox("Write practice notes")
with col4:
    c4 = st.checkbox("Save one career sentence")
progress = sum([c1, c2, c3, c4]) / 4
st.progress(progress)
st.write(f"Today progress: {int(progress * 100)} percent")

st.markdown("### Core Learning Areas")
a, b, c, d = st.columns(4)
with a:
    st.markdown("<div class='card'><div class='node'>01</div><b>Sampling and Research</b><br>Probability sampling nonprobability sampling surveys interviews focus groups and objective EMR data.</div>", unsafe_allow_html=True)
with b:
    st.markdown("<div class='card'><div class='node'>02</div><b>Workflow Intelligence</b><br>Documentation quality handoffs patient access staff efficiency and operational performance.</div>", unsafe_allow_html=True)
with c:
    st.markdown("<div class='card'><div class='node'>03</div><b>Denial Prevention</b><br>Documentation readiness payer friction authorization delays and upstream breakdowns.</div>", unsafe_allow_html=True)
with d:
    st.markdown("<div class='card'><div class='node'>04</div><b>Operational Visibility</b><br>Dashboards reports queues escalation signals and performance tracking.</div>", unsafe_allow_html=True)

st.markdown("### Flashcard Review")
question, answer = flashcards[st.session_state.flash_index]
st.info(answer if st.session_state.show_answer else question)
fa, fb, fc = st.columns(3)
with fa:
    if st.button("Previous Card"):
        st.session_state.flash_index = (st.session_state.flash_index - 1) % len(flashcards)
        st.session_state.show_answer = False
with fb:
    if st.button("Flip Card"):
        st.session_state.show_answer = not st.session_state.show_answer
with fc:
    if st.button("Next Card"):
        st.session_state.flash_index = (st.session_state.flash_index + 1) % len(flashcards)
        st.session_state.show_answer = False
st.caption(f"Card {st.session_state.flash_index + 1} of {len(flashcards)}")

st.markdown("### Quick Quiz")
q = quiz[st.session_state.quiz_index]
st.write(q["q"])
selected = st.radio("Choose one answer", q["options"], key=f"quiz_{st.session_state.quiz_index}")
qa, qb = st.columns(2)
with qa:
    if st.button("Check Answer"):
        if selected == q["answer"]:
            st.session_state.quiz_score += 1
            st.success("Correct.")
        else:
            st.error(f"Review this one. Correct answer: {q['answer']}")
with qb:
    if st.button("Next Quiz Question"):
        st.session_state.quiz_index = (st.session_state.quiz_index + 1) % len(quiz)

st.write(f"Quiz score this session: {st.session_state.quiz_score}")
if st.button("Restart Quiz Score"):
    st.session_state.quiz_index = 0
    st.session_state.quiz_score = 0

st.markdown("### Practice Notes")
notes = st.text_area("Write the concept in your own words", height=180, placeholder="Example: Probability sampling matters because it gives every eligible person a known chance of being selected which makes the findings more trustworthy for healthcare decision making.")
if st.button("Save Practice Note"):
    st.session_state.saved_note = notes
    st.success("Practice note saved for this session.")
if "saved_note" in st.session_state and st.session_state.saved_note:
    st.markdown("### Saved Practice Note")
    st.write(st.session_state.saved_note)

st.markdown("### Career Language Builder")
concept = st.selectbox("Choose a concept to turn into career language", ["Probability sampling", "Nonprobability sampling", "EMR system reports", "Workflow intelligence", "Denial prevention", "Operational visibility"])
career_templates = {
    "Probability sampling": "I understand that stronger sampling improves the trustworthiness of healthcare research findings because the selected group better represents the larger population.",
    "Nonprobability sampling": "I understand that nonprobability sampling can be useful when time or access is limited, but the results may be less representative and should be interpreted carefully.",
    "EMR system reports": "I understand that EMR system reports can provide objective workflow evidence such as documentation completion time, missing fields, error rates, and turnaround delays.",
    "Workflow intelligence": "I use workflow intelligence to think through how handoffs, documentation quality, communication, and accountability affect healthcare operations performance.",
    "Denial prevention": "I view denial prevention as an upstream operations issue connected to documentation readiness, payer requirements, authorization workflows, and escalation timing.",
    "Operational visibility": "I understand operational visibility as the ability to make queue pressure, delays, risk, and performance signals clear enough for leaders to act before problems grow.",
}
st.text_area("Copy ready career sentence", career_templates[concept], height=100)

st.markdown("""
<div class='footer'>
  <div>Created by Kori Pickle</div>
  <div class='footer-signature'>Kori Pickle</div>
  <div>LinkedIn · GitHub</div>
</div>
""", unsafe_allow_html=True)
