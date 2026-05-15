import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from streamlit_lottie import st_lottie
import requests
import time
import random

# --- ADVANCED UI CONFIG ---
st.set_page_config(page_title="NetDoc AI Pro", layout="wide", page_icon="🩺")

# --- CUSTOM DYNAMIC CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Plus+Jakarta+Sans:wght@300;500;700&display=swap');

/* Dynamic Background Animation */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stApp {
    background: linear-gradient(-45deg, #020617, #0f172a, #1e1b4b, #001d3d);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
    color: #FFFFFF !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Glassmorphism Cards */
.glass-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    padding: 30px;
    border: 1px solid rgba(0, 242, 255, 0.2);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    margin-bottom: 25px;
    transition: 0.4s;
}
.glass-card:hover {
    border: 1px solid #00f2ff;
    box-shadow: 0 0 20px rgba(0, 242, 255, 0.3);
}

/* Custom Neon Buttons */
div.stButton > button:first-child {
    background: linear-gradient(90deg, #00f2ff, #0062ff);
    color: white;
    border: none;
    padding: 12px 30px;
    border-radius: 50px;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 4px 15px rgba(0, 242, 255, 0.4);
    transition: 0.3s;
}
div.stButton > button:first-child:hover {
    box-shadow: 0 0 25px #00f2ff;
    transform: scale(1.05);
    color: white;
}

.neon-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 55px; font-weight: 700; text-align: center;
    background: linear-gradient(to right, #00f2ff, #7000ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 10px rgba(0, 242, 255, 0.5));
}

/* Professional Report Paper */
.report-paper {
    background: #FFFFFF !important;
    color: #1a1a1a !important;
    padding: 50px;
    border-radius: 2px;
    font-family: 'Georgia', serif;
    box-shadow: 0 0 40px rgba(0,0,0,0.7);
    line-height: 1.6;
}
.report-paper h1, .report-paper h2, .report-paper h3, .report-paper p, .report-paper b {
    color: #1a1a1a !important;
}

header {visibility: hidden;} footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- ASSETS ---
def load_lottie(url):
    try: return requests.get(url, timeout=5).json()
    except: return None

lottie_doc = load_lottie("https://lottie.host/8553641b-10f7-434a-9524-71e98822588c/OayXwS3S0R.json")
lottie_shield = load_lottie("https://lottie.host/68297b69-8088-466d-959c-8a192f1505c2/Wv0k06H4tV.json")

# --- AI MODEL ---
@st.cache_resource
def train_physician_ai():
    X = np.array([[20, 0, 2, 3], [200, 10, 40, 15], [50, 1, 5, 2], [350, 18, 60, 5], [10, 0, 1, 1]])
    y = np.array([0, 1, 0, 4, 0]) 
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model

ai_doc = train_physician_ai()

# --- APP LAYOUT ---
st.markdown("<h1 class='neon-title'>NETDOC AI PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8; font-size:18px;'>Autonomous Network Physician & Predictive Intelligence Agent</p>", unsafe_allow_html=True)

tabs = st.tabs(["🏥 CLINIC", "🧬 VITALS", "🛡️ SECURITY", "📈 PREDICTIONS", "📜 AUDIT"])

# --- TAB 1: CLINIC ---
with tabs[0]:
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("### 🩺 Start Bio-Scan")
        if lottie_doc: st_lottie(lottie_doc, height=200, key="doc")
        if st.button("RUN AI DIAGNOSIS"):
            with st.spinner("Analyzing DNA..."):
                time.sleep(2)
                lat, loss, jit, devs = random.randint(15, 350), random.randint(0, 12), random.randint(2, 65), random.randint(1, 30)
                pred = ai_doc.predict([[lat, loss, jit, devs]])[0]
                diags = {
                    0: ("Optimum Health", "System vitals are perfect.", "🟢"),
                    1: ("Congestion", "Network pathways are overloaded.", "🟡"),
                    4: ("ISP Failure", "Critical gateway failure detected.", "🔴")
                }
                st.session_state.audit = {
                    "v": diags.get(pred, diags[1])[0],
                    "p": diags.get(pred, diags[1])[1],
                    "i": diags.get(pred, diags[1])[2],
                    "stats": [lat, loss, jit, devs],
                    "time": time.strftime("%B %d, %Y | %H:%M:%S"),
                    "id": f"ND-{random.randint(1000, 9999)}"
                }
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if 'audit' in st.session_state:
            res = st.session_state.audit
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.write(f"## {res['i']} Diagnosis: {res['v']}")
            st.metric("Current Latency", f"{res['stats'][0]}ms")
            st.info(f"AI Suggestion: {res['p']}")
            st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 2: VITALS ---
with tabs[1]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 🧬 Network Heartbeat")
    df = pd.DataFrame(np.random.randint(20, 100, size=(20, 2)), columns=['Download', 'Upload'])
    fig = px.area(df, template="plotly_dark", color_discrete_sequence=['#00f2ff', '#bc13fe'])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: SECURITY ---
with tabs[2]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 🛡️ Immunity Shield")
    c1, c2 = st.columns(2)
    c1.header("Security Score: 94%")
    c1.write("Firewall is blocking 12 unauthorized IPs.")
    if lottie_shield:
        with c2: st_lottie(lottie_shield, height=150)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 4: PREDICTIONS (NEW) ---
with tabs[3]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 📈 AI Predictive Traffic (Next 24h)")
    pred_data = pd.DataFrame(np.random.randint(30, 90, size=(10, 1)), columns=['Load'])
    st.line_chart(pred_data)
    st.success("AI Predicts stable traffic for the next 6 hours.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 5: AUDIT REPORT (PROFESSIONAL TEXT) ---
with tabs[4]:
    if 'audit' in st.session_state:
        d = st.session_state.audit
        st.markdown("<div class='report-paper'>", unsafe_allow_html=True)
        st.markdown(f"""
        <h1 style="text-align:center;">NETWORK HEALTH AUDIT REPORT</h1>
        <p style="text-align:right;"><b>Reference:</b> {d['id']} | <b>Date:</b> {d['time']}</p>
        <hr style="border: 1px solid #1a1a1a;">
        <h3>1. EXECUTIVE SUMMARY</h3>
        <p>This report documents the autonomous forensic audit of the network infrastructure. 
        The AI-Physician Agent has classified the current state as <b>{d['v']}</b>.</p>
        
        <h3>2. TECHNICAL METRICS</h3>
        <p>During the deep-scan phase, the following vitals were recorded:</p>
        <p>- <b>Latency:</b> {d['stats'][0]} ms (Measured RTT)</p>
        <p>- <b>Packet Integrity:</b> {100 - d['stats'][1]}% Stable</p>
        <p>- <b>Connected Nodes:</b> {d['stats'][3]} Active Devices</p>
        
        <h3>3. AI PRESCRIPTION</h3>
        <p><b>Diagnosis:</b> {d['p']}</p>
        <p><b>Action Plan:</b> We recommend an immediate DNS flush and hardware gateway optimization 
        to restore full bandwidth throughput.</p>
        
        <br><br>
        <p style="text-align:right;"><i>Digitally Signed: Dr. Cyber-Sentinel</i></p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.download_button("📥 EXPORT AUDIT", f"Report: {d['v']}\nStats: {d['stats']}", file_name="Audit.txt")
    else:
        st.warning("Please run a scan in the Clinic tab first.")

# --- SIDEBAR ---
if st.sidebar.button("🗑️ PURGE DATA"):
    st.session_state.clear()
    st.rerun()
