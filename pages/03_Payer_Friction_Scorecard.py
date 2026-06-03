import streamlit as st
import pandas as pd

st.set_page_config(page_title="Payer Friction Scorecard", page_icon="🟠", layout="wide")

TENNESSEE_ORANGE = "#FF8200"
BLACK = "#000000"
WARM_GRAY = "#E8E3DC"

st.markdown("""
<style>
.stApp { background-color: #FFFFFF; color: #000000; }
.main .block-container { max-width: 1220px; padding-top: 2.2rem; padding-bottom: 3rem; }
h1, h2, h3 { font-family: Georgia, serif; letter-spacing: -0.03em; color: #000000; }
.kori-hero { border-bottom: 2px solid #FF8200; padding-bottom: 1.4rem; margin-bottom: 2rem; }
.kori-signature { font-family: Brush Script MT, Segoe Script, cursive; font-size: 3.4rem; color: #000000; line-height: 1; }
.kori-kicker { color: #FF8200; text-transform: uppercase; letter-spacing: .22em; font-size: .78rem; font-weight: 800; }
.kori-title { font-family: Georgia, serif; font-size: 3.6rem; line-height: 1; color: #000000; margin-top: .25rem; }
.orange { color: #FF8200; }
.card { border: 1px solid #E8E3DC; background: #FFFFFF; padding: 1.2rem; border-radius: 18px; box-shadow: 0 10px 30px rgba(0,0,0,.04); min-height: 145px; }
.metric-card { border: 1px solid #E8E3DC; background: #FFFFFF; padding: 1.2rem; border-radius: 18px; box-shadow: 0 10px 30px rgba(0,0,0,.04); text-align: center; }
.big-score { font-family: Georgia, serif; font-size: 4.6rem; line-height: .95; color: #FF8200; }
.node { width: 48px; height: 48px; border-radius: 50%; border: 3px solid #FF8200; box-shadow: 0 0 0 8px rgba(255,130,0,.08); display:flex; align-items:center; justify-content:center; color:#FF8200; font-weight:800; margin-bottom:.75rem; }
.footer { border-top: 1px solid #E8E3DC; margin-top: 3rem; padding-top: 1.5rem; text-align: center; color: #555; }
.footer-signature { font-family: Brush Script MT, Segoe Script, cursive; font-size: 2.8rem; color: #111; }
.warning-box { border-left: 5px solid #FF8200; background: rgba(255,130,0,.06); padding: 1rem 1.2rem; border-radius: 12px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='kori-hero'>
  <div class='kori-signature'>Kori Pickle</div>
  <div class='kori-kicker'>Healthcare Operations Intelligence</div>
  <div class='kori-title'>Payer Friction <span class='orange'>Scorecard</span></div>
</div>
""", unsafe_allow_html=True)

st.write("This interactive tool estimates payer friction using sample operational inputs. It is designed to demonstrate how authorization delays, documentation requests, denials, peer to peer volume, delayed cases, and revenue exposure can be translated into a simple leadership visibility score.")

st.markdown("### What This Tool Measures")
col_a, col_b, col_c, col_d = st.columns(4)
with col_a:
    st.markdown("<div class='card'><div class='node'>01</div><b>Turnaround Pressure</b><br>Measures how long authorizations are taking compared with a reasonable workflow threshold.</div>", unsafe_allow_html=True)
with col_b:
    st.markdown("<div class='card'><div class='node'>02</div><b>Documentation Friction</b><br>Measures repeated requests, missing information, and rework created before submission or approval.</div>", unsafe_allow_html=True)
with col_c:
    st.markdown("<div class='card'><div class='node'>03</div><b>Escalation Burden</b><br>Measures peer to peer requests and delayed cases that require extra coordination.</div>", unsafe_allow_html=True)
with col_d:
    st.markdown("<div class='card'><div class='node'>04</div><b>Revenue Exposure</b><br>Measures financial risk tied to authorization instability and payer behavior.</div>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("### Payer Inputs")
left, right = st.columns([1, 1])

with left:
    payer_name = st.text_input("Payer name", value="Humana")
    service_line = st.selectbox("Service line", ["Orthopedics", "Cardiology", "Rehabilitation", "Imaging", "Oncology", "Behavioral Health", "General Surgery", "Other"])
    auth_days = st.slider("Average authorization turnaround time in days", 0, 30, 9)
    denial_rate = st.slider("Denial rate percent", 0, 60, 18)
    delayed_cases = st.slider("Delayed active cases", 0, 500, 72)

with right:
    documentation_requests = st.slider("Documentation requests this period", 0, 300, 84)
    peer_to_peer = st.slider("Peer to peer requests this period", 0, 100, 14)
    revenue_at_risk = st.number_input("Estimated revenue at risk", min_value=0, max_value=5000000, value=487000, step=1000)
    staff_capacity = st.slider("Authorization team capacity used percent", 0, 250, 136)
    payer_trend = st.selectbox("Current payer trend", ["Stable", "Increasing friction", "Severe instability", "Improving"])

# scoring model
turnaround_score = min(auth_days / 14 * 25, 25)
denial_score = min(denial_rate / 30 * 20, 20)
documentation_score = min(documentation_requests / 120 * 18, 18)
peer_score = min(peer_to_peer / 30 * 12, 12)
delay_score = min(delayed_cases / 150 * 10, 10)
revenue_score = min(revenue_at_risk / 750000 * 10, 10)
capacity_score = min(max(staff_capacity - 100, 0) / 80 * 5, 5)
trend_bonus = {"Stable": 0, "Increasing friction": 5, "Severe instability": 10, "Improving": -5}[payer_trend]

friction_score = round(max(0, min(100, turnaround_score + denial_score + documentation_score + peer_score + delay_score + revenue_score + capacity_score + trend_bonus)))

if friction_score >= 80:
    risk_level = "Severe Payer Friction"
    risk_color = "#C7351A"
    priority = "High priority leadership review"
elif friction_score >= 60:
    risk_level = "High Payer Friction"
    risk_color = "#FF8200"
    priority = "Weekly operational review"
elif friction_score >= 40:
    risk_level = "Moderate Payer Friction"
    risk_color = "#B36B00"
    priority = "Monitor and trend weekly"
else:
    risk_level = "Controlled Payer Friction"
    risk_color = "#176B3A"
    priority = "Routine monitoring"

score_components = {
    "Authorization turnaround time": turnaround_score,
    "Denial rate": denial_score,
    "Documentation requests": documentation_score,
    "Peer to peer requests": peer_score,
    "Delayed cases": delay_score,
    "Revenue at risk": revenue_score,
    "Team capacity pressure": capacity_score,
    "Trend adjustment": trend_bonus,
}
main_driver = max(score_components, key=score_components.get)

if main_driver == "Authorization turnaround time":
    action = "Review the payer weekly and separate aging authorizations by service line, dollar exposure, and escalation status. Prioritize cases that are close to procedure date or tied to high revenue exposure."
elif main_driver == "Denial rate":
    action = "Audit recent denials by reason code, service line, and documentation pattern. Identify whether the denial starts in eligibility, prior authorization, clinical documentation, coding, or payer policy interpretation."
elif main_driver == "Documentation requests":
    action = "Create a payer specific documentation readiness checklist. Track repeat requests and build a pre submission review process for the most common missing items."
elif main_driver == "Peer to peer requests":
    action = "Track peer to peer triggers by payer and service line. Build an escalation workflow so high risk cases are routed to the right clinical owner early."
elif main_driver == "Delayed cases":
    action = "Segment delayed cases by age, service line, payer, and procedure date. Escalate aging cases before they become access delays, cancellations, or denials."
elif main_driver == "Revenue at risk":
    action = "Prioritize the highest dollar cases and connect payer friction reporting to revenue cycle leadership review. Focus on preventing avoidable write offs and delayed reimbursement."
elif main_driver == "Team capacity pressure":
    action = "Review staffing load, queue ownership, and escalation volume. Determine whether payer friction is creating unsustainable authorization workload."
else:
    action = "Review current payer trend and compare it with prior weeks to determine whether friction is isolated or becoming a pattern."

st.markdown("---")
st.markdown("### Scorecard Results")
r1, r2, r3 = st.columns([1, 1, 1])
with r1:
    st.markdown(f"<div class='metric-card'><div class='big-score'>{friction_score}</div><b>Friction Score</b><br>Out of 100</div>", unsafe_allow_html=True)
with r2:
    st.markdown(f"<div class='metric-card'><div style='font-family:Georgia,serif;font-size:2rem;color:{risk_color};'>{risk_level}</div><b>Risk Level</b><br>{priority}</div>", unsafe_allow_html=True)
with r3:
    st.markdown(f"<div class='metric-card'><div style='font-family:Georgia,serif;font-size:2rem;color:#000;'>{main_driver}</div><b>Main Friction Driver</b><br>Largest contributor to score</div>", unsafe_allow_html=True)

st.markdown("### Recommended Operational Action")
st.markdown(f"<div class='warning-box'><b>{payer_name} · {service_line}</b><br>{action}</div>", unsafe_allow_html=True)

st.markdown("### Suggested Owner and Review Cadence")
owner_col, cadence_col, signal_col = st.columns(3)
with owner_col:
    st.markdown("<div class='card'><b>Best Owner</b><br>Prior Authorization Supervisor, Revenue Cycle Manager, and Patient Access Leadership.</div>", unsafe_allow_html=True)
with cadence_col:
    st.markdown(f"<div class='card'><b>Review Cadence</b><br>{priority}. Use weekly trend review when the score is above 60.</div>", unsafe_allow_html=True)
with signal_col:
    st.markdown("<div class='card'><b>Risk Signal</b><br>High friction means the payer may be creating preventable rework, access delays, staff burden, or denial exposure.</div>", unsafe_allow_html=True)

st.markdown("### Score Breakdown")
breakdown_df = pd.DataFrame({
    "Component": list(score_components.keys()),
    "Weighted Points": [round(v, 1) for v in score_components.values()],
})
st.bar_chart(breakdown_df.set_index("Component"))
st.dataframe(breakdown_df, use_container_width=True, hide_index=True)

st.markdown("### Copy Ready Portfolio Explanation")
portfolio_text = f"""I built this Payer Friction Scorecard to demonstrate how payer behavior can be translated into operational visibility before denials occur. The tool uses sample inputs such as authorization turnaround time, denial rate, documentation requests, peer to peer volume, delayed cases, revenue at risk, and staff capacity pressure to generate a payer friction score. The purpose is not to represent payer policy or clinical medical necessity criteria. The purpose is to show how healthcare operations leaders can identify which payer relationships are creating the most workflow pressure, patient access risk, staff burden, and revenue cycle exposure."""
st.text_area("Portfolio explanation", portfolio_text, height=170)

st.markdown("### Disclaimer")
st.info("This is a portfolio demonstration tool using sample scoring logic. It does not represent payer policy, medical necessity rules, clinical decision making, or official reimbursement guidance.")

st.markdown("""
<div class='footer'>
  <div>Created by Kori Pickle</div>
  <div class='footer-signature'>Kori Pickle</div>
  <div>Healthcare Operations Intelligence · Workflow Intelligence · Denial Prevention · Operational Visibility</div>
</div>
""", unsafe_allow_html=True)
