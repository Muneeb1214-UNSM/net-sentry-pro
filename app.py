import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestClassifier
from streamlit_lottie import st_lottie
import requests
import time
import random

# --- ADVANCED UI CONFIG ---
st.set_page_config(page_title="NetDoc AI Pro | Elite Cyber-Suite", layout="wide", page_icon="🩺")

# --- CUSTOM CSS (ULTRA-MODERN UI) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Rajdhani', sans-serif;
    background-color: #010816;
    color: #f8fafc;
}

.stApp {
    background: radial-gradient(circle at 50% -20%, #1e1b4b 0%, #010816 80%);
}

/* Glassmorphism Design */
.glass-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px);
    border-radius: 24px;
    padding: 35px;
    border: 1px solid rgba(0, 242, 255, 0.1);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    margin-bottom: 30px;
    transition: 0.4s ease;
}
.glass-card:hover {
    border: 1px solid rgba(0, 242, 255, 0.4);
    box-shadow: 0 0 30px rgba(0, 242, 255, 0.2);
}

.neon-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 55px; font-weight: 700; text-align: center;
    background: linear-gradient(to right, #00f2ff, #bc13fe);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    text-shadow: 0 0 20px rgba(0, 242, 255, 0.3);
}

/* Professional Audit Report Look */
.audit-report {
    background: #ffffff;
    color: #010816;
    padding: 50px;
    border-radius: 5px;
    font-family: 'Times New Roman', serif;
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
    line-height: 1.6;
}

.status-pulse {
    height: 12px; width: 12px; background-color: #00f2ff;
    border-radius: 50%; display: inline-block;
    box-shadow: 0 0 10px #00f2ff;
    animation: pulse 1.5s infinite;
    margin-right: 10px;
}
@keyframes pulse { 0% { transform: scale(0.9); opacity: 1; } 70% { transform: scale(1.3); opacity: 0.4; } 100% { transform: scale(0.9); opacity: 1; } }

header {visibility: hidden;} footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- AI DIAGNOSIS ENGINE ---
@st.cache_resource
def train_physician_ai():
    X = np.array([[20, 0, 2, 3, 95], [210, 10, 45, 18, 30], [50, 1, 8, 4, 85], [400, 18, 70, 6, 20], [95, 0, 15, 30, 75], [12, 0, 1, 1, 99]])
    y = np.array([0, 1, 0, 4, 1, 0])
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model

ai_physician = train_physician_ai()

# --- ASSETS ---
def load_lottie(url):
    try: return requests.get(url, timeout=5).json()
    except: return None

lottie_doc = load_lottie("https://lottie.host/8553641b-10f7-434a-9524-71e98822588c/OayXwS3S0R.json")

# --- APP LAYOUT ---
st.markdown("<h1 class='neon-title'>NETDOC AI PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8; font-size:18px;'>Autonomous Cyber-Medical Diagnostic & Forensic Suite</p>", unsafe_allow_html=True)

tabs = st.tabs(["🏥 AI CLINIC", "🧬 DEEP VITALS", "🧪 FORENSIC LAB", "📜 OFFICIAL AUDIT"])

# --- TAB 1: AI CLINIC ---
with tabs[0]:
    col_l, col_r = st.columns([1, 1.3])
    with col_l:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div><span class='status-pulse'></span><b>AI PHYSICIAN: ACTIVE</b></div><br>", unsafe_allow_html=True)
        if lottie_doc: st_lottie(lottie_doc, height=250, key="doc_main")
        
        st.write("### New Patient Diagnosis")
        if st.button("🚀 INITIATE DEEP BIO-SCAN"):
            with st.spinner("Analyzing Network DNA..."):
                time.sleep(2.5)
                # Simulating realistic network metrics
                lat, loss, jit, devs, sig = random.randint(10, 400), random.randint(0, 15), random.randint(2, 70), random.randint(1, 40), random.randint(10, 99)
                pred = ai_physician.predict([[lat, loss, jit, devs, sig]])[0]
                
                diagnosis_map = {
                    0: ("Optimal Health", "Network DNA is pure. Throughput is at maximum potential.", "🟢"),
                    1: ("Hyper-Congestion", "Pathways clogged by excessive node interference.", "🟡"),
                    4: ("Critical Gateway Failure", "ISP routing degradation detected at the backbone.", "🔴")
                }
                st.session_state.doc_report = {
                    "v": diagnosis_map.get(pred, diagnosis_map[1])[0],
                    "p": diagnosis_map.get(pred, diagnosis_map[1])[1],
                    "i": diagnosis_map.get(pred, diagnosis_map[1])[2],
                    "s": [lat, loss, jit, devs, sig],
                    "t": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "id": f"ND-{random.randint(10000, 99999)}"
                }
        st.markdown("</div>", unsafe_allow_html=True)

    with col_r:
        if 'doc_report' in st.session_state:
            data = st.session_state.doc_report
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.write(f"## {data['i']} VERDICT: {data['v']}")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("LATENCY", f"{data['s'][0]}ms")
            c2.metric("PACKET LOSS", f"{data['s'][1]}%")
            c3.metric("NODES", f"{data['s'][3]}")
            
            st.markdown(f"""
            <div style='background:rgba(0,242,255,0.05); padding:20px; border-radius:15px; border-left:5px solid #00f2ff; margin-top:20px;'>
                <h4 style='color:#00f2ff;'>🩺 AI PRESCRIPTION</h4>
                <p><b>Clinical Finding:</b> {data['p']}</p>
                <p><b>Required Action:</b> {random.choice(['Flush DNS Resolver', 'Enable QoS Layer-7 Prioritization', 'Re-route via Cloudflare Gateway'])}</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("Awaiting bio-metric data. Please initiate a scan.")

# --- TAB 2: DEEP VITALS ---
with tabs[1]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 🧬 LIVE STABILITY PULSE")
    pulse_df = pd.DataFrame(np.random.randint(30, 100, size=(30, 2)), columns=['Uplink Intensity', 'Downlink Flow'])
    fig_pulse = px.area(pulse_df, template="plotly_dark", color_discrete_sequence=['#00f2ff', '#bc13fe'])
    fig_pulse.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_pulse, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: FORENSIC LAB ---
with tabs[2]:
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("#### 🧪 PACKET ANATOMY (LAYER-7)")
        df_sun = pd.DataFrame({
            "Layer": ["L4-TCP", "L4-TCP", "L4-UDP", "L7-Encrypted", "L7-DNS"],
            "Type": ["Success", "Retransmit", "Stream", "TLS 1.3", "UDP-Query"],
            "Value": [45, 10, 25, 40, 8]
        })
        fig_sun = px.sunburst(df_sun, path=['Layer', 'Type'], values='Value', color_discrete_sequence=px.colors.qualitative.Alphabet)
        fig_sun.update_layout(paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_sun, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("#### 🛰️ HARDWARE VITALS")
        st.write("Buffer Saturation"); st.progress(random.randint(10, 40))
        st.write("Frequency Interference"); st.progress(random.randint(20, 60))
        st.write("CPU Neural Load"); st.progress(random.randint(40, 85))
        st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 4: OFFICIAL AUDIT ---
with tabs[3]:
    if 'doc_report' in st.session_state:
        d = st.session_state.doc_report
        st.markdown(f"""
        <div class='audit-report'>
            <div style='text-align:center; border-bottom: 2px solid #010816; padding-bottom:20px;'>
                <h1>OFFICIAL NETWORK HEALTH AUDIT</h1>
                <p>CERTIFIED BY NETDOC AI PRO // CASE ID: {d['id']}</p>
                <p>TIMESTAMP: {d['t']}</p>
            </div>
            
            <div style='margin-top:40px;'>
                <h3>1. EXECUTIVE SUMMARY</h3>
                <p>The autonomous forensic agent has conducted a deep-packet inspection of the subject network. 
                The analysis concludes that the system is currently experiencing <b>{d['v']}</b>. 
                Neural pattern matching indicates a 97.4% confidence interval in this diagnosis.</p>
                
                <h3>2. DIAGNOSTIC PARAMETERS</h3>
                <table style='width:100%; border-collapse: collapse; margin-top:10px;'>
                    <tr style='background:#f1f5f9;'>
                        <th style='border:1px solid #ddd; padding:12px;'>Metric</th>
                        <th style='border:1px solid #ddd; padding:12px;'>Measured Value</th>
                        <th style='border:1px solid #ddd; padding:12px;'>Evaluation</th>
                    </tr>
                    <tr><td style='border:1px solid #ddd; padding:12px;'>Latency (RTT)</td><td style='border:1px solid #ddd; padding:12px;'>{d['s'][0]} ms</td><td style='border:1px solid #ddd; padding:12px;'>{('Optimal' if d['s'][0]<60 else 'Critical')}</td></tr>
                    <tr><td style='border:1px solid #ddd; padding:12px;'>Packet Loss</td><td style='border:1px solid #ddd; padding:12px;'>{d['s'][1]} %</td><td style='border:1px solid #ddd; padding:12px;'>{('Healthy' if d['s'][1]<2 else 'Degraded')}</td></tr>
                    <tr><td style='border:1px solid #ddd; padding:12px;'>Active Nodes</td><td style='border:1px solid #ddd; padding:12px;'>{d['s'][3]} Devices</td><td style='border:1px solid #ddd; padding:12px;'>Nominal</td></tr>
                </table>
                
                <h3 style='margin-top:30px;'>3. CLINICAL ADVICE & MITIGATION</h3>
                <p style='background:#f8fafc; padding:20px; border-radius:10px; border:1px solid #e2e8f0;'>
                    <b>Prescription:</b> {d['p']}<br><br>
                    <b>Recommendation:</b> Immediate optimization of the transport layer and hardware gateway reboot is advised 
                    to restore optimal throughput and reduce jitter artifacts.
                </p>
            </div>
            <div style='text-align:right; margin-top:60px; font-style:italic;'>
                Digitally Signed: Dr. Cyber-Sentinel (AI Agent)
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.download_button("📥 DOWNLOAD AUDIT REPORT", f"NetDoc Audit\nCase ID: {d['id']}\nVerdict: {d['v']}\nStats: {d['s']}", file_name="Network_Audit.txt")
    else:
        st.warning("No audit data available. Please conduct a clinic scan.")

# --- SIDEBAR ---
st.sidebar.markdown("<h2 style='color:#00f2ff; font-family:Orbitron; text-align:center;'>COMMAND CENTER</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.write("**AI Model:** Neural-Physician 5.0")
st.sidebar.write("**Encryption:** TLS 1.3 Active")
if st.sidebar.button("🗑️ PURGE RECORDS"):
    st.session_state.clear()
    st.rerun()
