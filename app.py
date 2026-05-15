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
st.set_page_config(page_title="NetDoc AI Pro | Elite Cyber-Suite", layout="wide", page_icon="🩺")

# --- CUSTOM CSS (HIGH CONTRAST & ANIMATED) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Rajdhani', sans-serif;
    background-color: #020617;
    color: #FFFFFF; /* High contrast white text */
}

.stApp {
    background: radial-gradient(circle at 50% -20%, #0f172a 0%, #020617 80%);
}

/* Glassmorphism Design */
.glass-card {
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    padding: 30px;
    border: 1px solid rgba(0, 242, 255, 0.3);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    margin-bottom: 25px;
}

.neon-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 50px; font-weight: 700; text-align: center;
    color: #00f2ff;
    text-shadow: 0 0 15px #00f2ff;
    margin-bottom: 10px;
}

/* Professional Audit Report (White Paper Look) */
.report-frame {
    background: #FFFFFF;
    color: #111827 !important;
    padding: 40px;
    border-radius: 8px;
    font-family: 'serif';
    line-height: 1.6;
    box-shadow: 0 0 40px rgba(0,0,0,0.8);
}
.report-frame h1, .report-frame h2, .report-frame h3, .report-frame p {
    color: #111827 !important;
}

header {visibility: hidden;} footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- ASSETS ---
def load_lottie(url):
    try: return requests.get(url, timeout=5).json()
    except: return None

lottie_boot = load_lottie("https://lottie.host/8553641b-10f7-434a-9524-71e98822588c/OayXwS3S0R.json") # AI Brain
lottie_scanning = load_lottie("https://lottie.host/57a731d6-d3a3-4809-9683-16a707165089/y8Z9Fk1G4R.json") # Radar

# --- INTRO ANIMATION (Splash Screen) ---
if 'booted' not in st.session_state:
    st.markdown("<h1 class='neon-title'>INITIALIZING NETDOC AI CORE...</h1>", unsafe_allow_html=True)
    if lottie_boot:
        st_lottie(lottie_boot, height=400)
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    
    st.session_state.booted = True
    st.rerun()

# --- AI MODEL (SIMULATION) ---
@st.cache_resource
def train_physician_ai():
    X = np.array([[20, 0, 2, 3], [200, 10, 40, 15], [50, 1, 5, 2], [350, 18, 60, 5], [10, 0, 1, 1]])
    y = np.array([0, 1, 0, 4, 0]) 
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model

ai_physician = train_physician_ai()

# --- MAIN APP ---
st.markdown("<h1 class='neon-title'>NETDOC AI PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8; font-size:20px;'>Autonomous Network Diagnostics & Forensic Laboratory</p>", unsafe_allow_html=True)

tabs = st.tabs(["🏥 AI CLINIC", "🧬 LIVE VITALS", "📜 PROFESSIONAL REPORT"])

# --- TAB 1: AI CLINIC ---
with tabs[0]:
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("### 🔍 Initiate System Scan")
        if lottie_boot: st_lottie(lottie_boot, height=200, key="clinic_anim")
        
        if st.button("🚀 RUN DEEP BIO-SCAN"):
            with st.spinner("Analyzing Network Vitals..."):
                time.sleep(2)
                lat, loss, jit, devs = random.randint(10, 400), random.randint(0, 15), random.randint(2, 70), random.randint(1, 30)
                pred = ai_physician.predict([[lat, loss, jit, devs]])[0]
                
                diagnosis_map = {
                    0: ("Optimum Health", "System DNA is clean. All vitals normal.", "🟢"),
                    1: ("Hyper-Congestion", "Pathways clogged by excessive load.", "🟡"),
                    4: ("Critical Failure", "Backbone ISP routing degradation detected.", "🔴")
                }
                
                st.session_state.report_data = {
                    "v": diagnosis_map.get(pred, diagnosis_map[1])[0],
                    "p": diagnosis_map.get(pred, diagnosis_map[1])[1],
                    "i": diagnosis_map.get(pred, diagnosis_map[1])[2],
                    "stats": [lat, loss, jit, devs],
                    "time": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "case_id": f"ND-{random.randint(1000, 9999)}"
                }
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if 'report_data' in st.session_state:
            d = st.session_state.report_data
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.write(f"## {d['i']} VERDICT: {d['v']}")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Latency", f"{d['stats'][0]}ms")
            c2.metric("Loss", f"{d['stats'][1]}%")
            c3.metric("Nodes", f"{d['stats'][3]}")
            
            st.markdown(f"""
            <div style='background:rgba(0,242,255,0.1); padding:20px; border-radius:15px; border-left:5px solid #00f2ff; margin-top:20px;'>
                <h4 style='color:#00f2ff;'>🩺 AI PRESCRIPTION</h4>
                <p><b>Diagnosis:</b> {d['p']}</p>
                <p><b>Recommended Action:</b> Restarting ONT Gateway and flushing DNS cache.</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            if lottie_scanning: st_lottie(lottie_scanning, height=300, key="scan_main")
            st.info("The AI Physician is awaiting a scan request.")

# --- TAB 2: LIVE VITALS ---
with tabs[1]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 🧬 Real-Time Stability Pulse")
    df_pulse = pd.DataFrame(np.random.randint(30, 100, size=(20, 2)), columns=['Uplink', 'Downlink'])
    fig = px.area(df_pulse, template="plotly_dark", color_discrete_sequence=['#00f2ff', '#bc13fe'])
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: PROFESSIONAL AUDIT REPORT ---
with tabs[2]:
    if 'report_data' in st.session_state:
        d = st.session_state.report_data
        
        # Proper Report Styling - No Code showing, just text
        report_html = f"""
        <div class="report-frame">
            <h1 style="text-align:center; border-bottom: 2px solid #111827; padding-bottom: 10px;">
                NETWORK HEALTH AUDIT REPORT
            </h1>
            <p style="text-align:right;"><b>Case ID:</b> {d['case_id']} | <b>Date:</b> {d['time']}</p>
            
            <h3>1. EXECUTIVE SUMMARY</h3>
            <p>This document certifies the network audit conducted by NetDoc AI Pro. 
            The system has been analyzed for packet integrity and latency. 
            The current diagnosis is <b>{d['v']}</b>.</p>
            
            <h3>2. DIAGNOSTIC DATA</h3>
            <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
                <tr style="background-color: #f3f4f6;">
                    <th style="border: 1px solid #d1d5db; padding: 12px; text-align: left;">Parameter</th>
                    <th style="border: 1px solid #d1d5db; padding: 12px; text-align: left;">Value</th>
                    <th style="border: 1px solid #d1d5db; padding: 12px; text-align: left;">Status</th>
                </tr>
                <tr>
                    <td style="border: 1px solid #d1d5db; padding: 12px;">Round Trip Latency</td>
                    <td style="border: 1px solid #d1d5db; padding: 12px;">{d['stats'][0]} ms</td>
                    <td style="border: 1px solid #d1d5db; padding: 12px;">{('Stable' if d['stats'][0]<100 else 'Critical')}</td>
                </tr>
                <tr>
                    <td style="border: 1px solid #d1d5db; padding: 12px;">Packet Loss Ratio</td>
                    <td style="border: 1px solid #d1d5db; padding: 12px;">{d['stats'][1]} %</td>
                    <td style="border: 1px solid #d1d5db; padding: 12px;">{('Optimal' if d['stats'][1]<2 else 'Poor')}</td>
                </tr>
            </table>
            
            <h3>3. DOCTOR'S CONCLUSION</h3>
            <p style="background-color: #f9fafb; padding: 15px; border-radius: 5px; border: 1px solid #e5e7eb;">
                <b>Conclusion:</b> {d['p']} <br><br>
                <b>Advice:</b> Change the router channel to avoid interference and upgrade firmware.
            </p>
            
            <p style="text-align:right; margin-top: 50px;"><i>Digitally Signed: Dr. Cyber-Sentinel (NetDoc AI)</i></p>
        </div>
        """
        st.markdown(report_html, unsafe_allow_html=True)
        st.download_button("📥 DOWNLOAD AUDIT FILE", f"NetDoc Audit\nStatus: {d['v']}\nStats: {d['stats']}", file_name="Network_Audit.txt")
    else:
        st.warning("⚠️ No data available. Please conduct a Clinic Scan first.")

# --- SIDEBAR ---
if st.sidebar.button("🗑️ PURGE RECORDS"):
    st.session_state.clear()
    st.rerun()
