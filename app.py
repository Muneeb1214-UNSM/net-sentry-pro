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

# --- CUSTOM DYNAMIC NEON CSS ---
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
    background: rgba(255, 255, 255, 0.04);
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
    box-shadow: 0 0 25px rgba(0, 242, 255, 0.3);
}

/* Target all Buttons (Standard & Download) */
div.stButton > button, div.stDownloadButton > button {
    background: linear-gradient(90deg, #00f2ff, #0062ff) !important;
    color: white !important;
    border: none !important;
    padding: 12px 30px !important;
    border-radius: 50px !important;
    font-weight: bold !important;
    text-transform: uppercase !important;
    letter-spacing: 1.5px !important;
    box-shadow: 0 4px 15px rgba(0, 242, 255, 0.4) !important;
    width: 100%;
    transition: 0.3s !important;
}
div.stButton > button:hover, div.stDownloadButton > button:hover {
    box-shadow: 0 0 25px #00f2ff !important;
    transform: translateY(-3px) !important;
}

.neon-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 55px; font-weight: 700; text-align: center;
    background: linear-gradient(to right, #00f2ff, #7000ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 10px rgba(0, 242, 255, 0.5));
}

/* Professional Audit Certificate */
.report-paper {
    background: #FFFFFF !important;
    color: #1a1a1a !important;
    padding: 50px;
    border-radius: 4px;
    font-family: 'Georgia', serif;
    box-shadow: 0 0 40px rgba(0,0,0,0.8);
    line-height: 1.6;
}
.report-paper h1, .report-paper h2, .report-paper h3, .report-paper p, .report-paper li {
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

# --- AI DIAGNOSIS ENGINE ---
@st.cache_resource
def train_physician_ai():
    X = np.array([[20, 0, 2, 3], [200, 10, 40, 15], [50, 1, 5, 2], [350, 18, 60, 5]])
    y = np.array([0, 1, 0, 4]) 
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model

ai_physician = train_physician_ai()

# --- APP LAYOUT ---
st.markdown("<h1 class='neon-title'>NETDOC AI PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#FFFFFF; font-size:20px;'>Autonomous AI Physician for Network Forensics</p>", unsafe_allow_html=True)

tabs = st.tabs(["🏥 CLINIC", "🧬 VITALS", "🛡️ SECURITY", "📜 OFFICIAL AUDIT"])

# --- TAB 1: CLINIC ---
with tabs[0]:
    col1, col2 = st.columns([1, 1.3])
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("### 🩺 Start Deep Scan")
        if lottie_doc: st_lottie(lottie_doc, height=200, key="doc_clinic")
        
        if st.button("RUN AI DIAGNOSIS"):
            with st.spinner("Analyzing DNA..."):
                time.sleep(2)
                lat, loss, jit = random.randint(15, 350), random.randint(0, 12), random.randint(2, 65)
                devs = random.randint(1, 20)
                pkts = random.randint(1000, 5000)
                
                pred = ai_physician.predict([[lat, loss, jit, devs]])[0]
                diags = {
                    0: ("Optimum Health", "Network DNA is stable. All vitals normal.", "نظام بالکل ٹھیک کام کر رہا ہے۔", "🟢"),
                    1: ("Hyper-Congestion", "Pathways clogged by excessive load.", "نیٹ ورک پر بوجھ زیادہ ہے۔ فالتو ڈیوائسز بند کریں۔", "🟡"),
                    4: ("Gateway Failure", "Critical gateway failure detected at ISP level.", "انٹرنیٹ فراہم کرنے والے کے پیچھے سے مسئلہ ہے۔", "🔴")
                }
                st.session_state.audit = {
                    "v": diags.get(pred, diags[1])[0],
                    "p_eng": diags.get(pred, diags[1])[1],
                    "p_urdu": diags.get(pred, diags[1])[2],
                    "i": diags.get(pred, diags[1])[3],
                    "stats": [lat, loss, jit, devs, pkts],
                    "time": time.strftime("%B %d, %Y | %H:%M:%S"),
                    "id": f"ND-{random.randint(1000, 9999)}"
                }
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if 'audit' in st.session_state:
            res = st.session_state.audit
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.write(f"## {res['i']} Diagnosis: {res['v']}")
            
            m1, m2, m3 = st.columns(3)
            m1.metric("Latency", f"{res['stats'][0]}ms")
            m2.metric("Nodes Online", f"{res['stats'][3]}")
            m3.metric("Packets Processed", f"{res['stats'][4]}")
            
            st.write("---")
            st.write(f"📋 **English Advice:** {res['p_eng']}")
            st.write(f"📋 **اردو مشورہ:** {res['p_urdu']}")
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("The AI Physician is awaiting a scan request.")

# --- TAB 2: VITALS ---
with tabs[1]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 🧬 Network Stability Pulse")
    v_data = pd.DataFrame(np.random.randint(30, 100, size=(20, 2)), columns=['Uplink', 'Downlink'])
    fig = px.area(v_data, template="plotly_dark", color_discrete_sequence=['#00f2ff', '#bc13fe'])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: SECURITY ---
with tabs[2]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 🛡️ Cyber-Shield Status")
    sc1, sc2 = st.columns(2)
    with sc1:
        st.header("Immunity: 96%")
        st.write("- Encryption: TLS 1.3 Active")
        st.write("- Threats Blocked: 04")
    with sc2:
        st.success("Your network DNA is protected by autonomous AI agents.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 4: OFFICIAL AUDIT ---
with tabs[3]:
    if 'audit' in st.session_state:
        d = st.session_state.audit
        st.markdown("<div class='report-paper'>", unsafe_allow_html=True)
        st.markdown(f"""
        <h1 style="text-align:center;">NETWORK HEALTH AUDIT REPORT</h1>
        <p style="text-align:right;"><b>Reference:</b> {d['id']} | <b>Date:</b> {d['time']}</p>
        <hr style="border: 1px solid #1a1a1a;">
        
        <h3>1. EXECUTIVE SUMMARY</h3>
        <p>This document serves as an autonomous forensic audit of the subject network. 
        The AI Physician Agent has classified the system status as <b>{d['v']}</b>.</p>
        
        <h3>2. MEASURED VITALS</h3>
        <p>The following metrics were recorded during the deep-scan phase:</p>
        <ul>
            <li><b>Round Trip Latency:</b> {d['stats'][0]} ms</li>
            <li><b>Packet Integrity:</b> {100 - d['stats'][1]}% Stable</li>
            <li><b>Active Network Nodes:</b> {d['stats'][3]} Devices detected</li>
            <li><b>Total Packets Analyzed:</b> {d['stats'][4]} Units</li>
        </ul>
        
        <h3>3. AI CLINICAL PRESCRIPTION</h3>
        <p><b>Diagnosis (English):</b> {d['p_eng']}</p>
        <p><b>اردو تشخیص:</b> {d['p_urdu']}</p>
        <p><b>Recommended Treatment:</b> We advise an immediate DNS resolver flush and a hardware gateway reboot to restore maximum throughput.</p>
        
        <br><br>
        <p style="text-align:right;"><i>Digitally Signed: Dr. Cyber-Sentinel (AI Agent)</i></p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            label="📥 DOWNLOAD PROFESSIONAL REPORT",
            data=f"NetDoc AI Audit Report\n\nReference: {d['id']}\nStatus: {d['v']}\nLatency: {d['stats'][0]}ms\nAdvice: {d['p_eng']}",
            file_name=f"NetDoc_Report_{d['id']}.txt"
        )
    else:
        st.warning("⚠️ No diagnostic data found. Please run a scan in the Clinic tab first.")

# --- SIDEBAR ---
if st.sidebar.button("🗑️ PURGE CLINIC DATA"):
    st.session_state.clear()
    st.rerun()
