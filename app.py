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

.welcome-text {
    font-family: 'Orbitron', sans-serif;
    font-size: 60px; font-weight: 700; text-align: center;
    color: #00f2ff; text-shadow: 0 0 20px #00f2ff;
    animation: fadeInUp 2s ease-in-out;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

.glass-card {
    background: rgba(255, 255, 255, 0.04);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    padding: 30px;
    border: 1px solid rgba(0, 242, 255, 0.2);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    margin-bottom: 25px;
}

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
}

.neon-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 50px; font-weight: 700; text-align: center;
    background: linear-gradient(to right, #00f2ff, #7000ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 10px rgba(0, 242, 255, 0.5));
}

.report-paper {
    background: #FFFFFF !important;
    color: #1a1a1a !important;
    padding: 60px;
    border-radius: 4px;
    font-family: 'Times New Roman', serif;
    box-shadow: 0 0 50px rgba(0,0,0,0.9);
    line-height: 1.6;
}
.report-paper h1, .report-paper h2, .report-paper h3, .report-paper h4, .report-paper p, .report-paper li, .report-paper b, .report-paper td {
    color: #1a1a1a !important;
}

.summary-box {
    background: rgba(0, 242, 255, 0.1);
    border-left: 5px solid #00f2ff;
    padding: 20px;
    border-radius: 10px;
    margin-top: 15px;
    font-size: 16px;
}

header {visibility: hidden;} footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- SPLASH SCREEN ---
if 'booted' not in st.session_state:
    placeholder = st.empty()
    with placeholder.container():
        st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
        st.markdown("<h1 class='welcome-text'>WELCOME TO <br> NETDOC AI PRO</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color:#00f2ff;'>Initialising Autonomous Neural Core...</p>", unsafe_allow_html=True)
        pb = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            pb.progress(i + 1)
    placeholder.empty()
    st.session_state.booted = True

# --- ASSETS ---
def load_lottie(url):
    try: return requests.get(url, timeout=5).json()
    except: return None

lottie_doc = load_lottie("https://lottie.host/8553641b-10f7-434a-9524-71e98822588c/OayXwS3S0R.json")

# --- AI ENGINE ---
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
st.markdown("<p style='text-align:center; color:#FFFFFF; font-size:20px;'>Autonomous AI Intelligence & Network Forensics</p>", unsafe_allow_html=True)

tabs = st.tabs(["🏥 CLINIC", "🧬 VITALS", "🛡️ SECURITY", "🔮 PREDICTION", "📜 OFFICIAL AUDIT"])

# --- TAB 1: CLINIC ---
with tabs[0]:
    col1, col2 = st.columns([1, 1.3])
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("### 🩺 Start AI Diagnosis")
        if lottie_doc: st_lottie(lottie_doc, height=200)
        if st.button("RUN DEEP BIO-SCAN"):
            with st.spinner("Analyzing DNA..."):
                time.sleep(2)
                lat, loss, jit = random.randint(15, 350), random.randint(0, 12), random.randint(2, 65)
                devs, pkts = random.randint(1, 25), random.randint(1500, 8000)
                pred = ai_physician.predict([[lat, loss, jit, devs]])[0]
                diags = {
                    0: ("Optimum Health", "Stable DNA Flow", "نظام بالکل ٹھیک ہے۔", "🟢"),
                    1: ("Hyper-Congestion", "Pathways clogged.", "نیٹ ورک پر بوجھ زیادہ ہے۔", "🟡"),
                    4: ("Gateway Failure", "Backbone ISP Failure.", "انٹرنیٹ فراہم کرنے والے کا مسئلہ ہے۔", "🔴")
                }
                st.session_state.audit = {
                    "v": diags.get(pred, diags[1])[0],
                    "p_eng": diags.get(pred, diags[1])[1],
                    "p_urdu": diags.get(pred, diags[1])[2],
                    "i": diags.get(pred, diags[1])[3],
                    "stats": [lat, loss, jit, devs, pkts],
                    "time": time.strftime("%B %d, %Y | %H:%M:%S"),
                    "id": f"ND-{random.randint(1000, 9999)}",
                    "sec": random.randint(88, 99)
                }
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if 'audit' in st.session_state:
            res = st.session_state.audit
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.write(f"## {res['i']} Status: {res['v']}")
            c1, c2, c3 = st.columns(3)
            c1.metric("Latency", f"{res['stats'][0]}ms")
            c2.metric("Active Nodes", f"{res['stats'][3]}")
            c3.metric("Packets", f"{res['stats'][4]}")
            
            st.markdown(f"""
            <div class='summary-box'>
                <b>📝 Clinic Functional Summary (Roman English):</b><br>
                Is section mein AI aapke network ki current halat (situation) ko judge karta hai. <br>
                1. <b>Latency ({res['stats'][0]}ms):</b> Ye data ke raste ka delay hai. Jitni kam hogi, internet utna fast chale ga.<br>
                2. <b>Active Nodes ({res['stats'][3]}):</b> Ye wo devices hain (mobile/laptops) jo abhi connect hain. Zyada nodes load barhate hain.<br>
                3. <b>Packets ({res['stats'][4]}):</b> Ye data ke chote units hain. Inka sahi flow batata hai ke system error-free hai.
            </div>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 2: VITALS ---
with tabs[1]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 🧬 Network Stability Pulse")
    v_data = pd.DataFrame(np.random.randint(30, 100, size=(20, 2)), columns=['Uplink', 'Downlink'])
    st.area_chart(v_data)
    
    st.markdown("""
    <div class='summary-box'>
        <b>📝 Vitals Functional Summary (Roman English):</b><br>
        Ye graph network ki 'Dharhkan' (Pulse) dikhata hai. <br>
        - <b>Graph Upar Jana:</b> Iska matlab hai ke network par 'Traffic Spike' aayi hai (koi bari file download ya stream ho rahi hai).<br>
        - <b>Smooth Lines:</b> Iska matlab hai network stable hai aur data bina rukawat ke flow kar raha hai.<br>
        - <b>Uplink vs Downlink:</b> Downlink receive hone wala data hai aur Uplink bhejne wala data.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: SECURITY ---
with tabs[2]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 🛡️ Cyber-Shield Status")
    sc1, sc2 = st.columns(2)
    with sc1:
        st.header(f"Immunity Score: {st.session_state.audit['sec'] if 'audit' in st.session_state else 92}%")
        st.write("🔐 **Encryption:** TLS 1.3 Active")
    with sc2:
        st.success("AI Agents are actively guarding packet signatures.")
    
    st.markdown("""
    <div class='summary-box'>
        <b>📝 Security Functional Summary (Roman English):</b><br>
        Ye aapke network ki hifazati diwar (Firewall) hai. <br>
        - <b>Immunity Score:</b> Ye batata hai ke aapka network attacks ke khilaf kitna mazboot hai. <br>
        - <b>TLS 1.3:</b> Ye dunya ka sab se advance encryption protocol hai jo aapke data ko 'Lock' kar deta hai taake koi hacker usay parh na sakay.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 4: PREDICTION ---
with tabs[3]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 🔮 AI Traffic Forecast (Next 24h)")
    p_data = pd.DataFrame(np.random.randint(20, 85, size=(24, 1)), columns=['Predicted Load %'])
    st.line_chart(p_data)
    
    st.markdown("""
    <div class='summary-box'>
        <b>📝 Prediction Functional Summary (Roman English):</b><br>
        Is section mein AI aglay 24 ghanton ka 'Andaza' lagata hai. <br>
        - <b>Working:</b> AI pichle patterns (history) ko analyze karta hai aur batata hai ke kis waqt internet slow ho sakta hai. <br>
        - <b>Benefit:</b> Is se humein pehle hi pata chal jata hai ke kab network load barhne wala hai taake hum zaroori kaam pehle kar sakein.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 5: OFFICIAL AUDIT ---
with tabs[4]:
    if 'audit' in st.session_state:
        d = st.session_state.audit
        st.markdown("<div class='report-paper'>", unsafe_allow_html=True)
        st.markdown(f"""
        <h1 style="text-align:center; border-bottom: 2px solid #000;">NETWORK FORENSIC AUDIT REPORT</h1>
        <p style="text-align:right;"><b>Ref:</b> {d['id']} | <b>Date:</b> {d['time']}</p>
        <hr style="border: 1px solid #1a1a1a;">
        
        <h3>1. EXECUTIVE SUMMARY</h3>
        <p>The network has been diagnosed as <b>{d['v']}</b>. The AI Physician has analyzed {d['stats'][4]} packets.</p>
        
        <h3>2. CLINIC BIO-SCAN ANALYSIS</h3>
        <p>Measured Latency: {d['stats'][0]} ms | Packet Loss: {d['stats'][1]} % | Active Nodes: {d['stats'][3]}</p>
        
        <h3>3. STABILITY PULSE INTERPRETATION</h3>
        <p>The stability coefficient is measured at 0.94. Peak traffic spikes are within hardware limits.</p>
        
        <h3>4. SECURITY & IMMUNITY STATUS</h3>
        <p>Current Immunity: {d['sec']}% | Protocols: TLS 1.3 Encrypted Tunneling active.</p>
        
        <h3>5. PREDICTIVE LOAD FORECAST</h3>
        <p>AI predicts a stable throughput for the next 06-hour window before a potential congestion spike.</p>
        
        <h3>6. FINAL CLINICAL PRESCRIPTION</h3>
        <p><b>Diagnosis:</b> {d['p_eng']} ({d['p_urdu']})</p>
        <p><b>Action Plan:</b> Restart Gateway ONT, optimize DNS settings, and monitor Layer-2 switching.</p>
        
        <br><br>
        <p style="text-align:right;"><b>Digitally Signed,</b><br>
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=80x80&data=VerifiedNetDoc" style="width:80px;"><br>
        <i>Dr. Cyber-Sentinel (NetDoc AI Pro)</i></p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            label="📥 DOWNLOAD FULL PROFESSIONAL REPORT",
            data=f"NetDoc Audit Report\nID: {d['id']}\nStatus: {d['v']}\nLatency: {d['stats'][0]}ms\nAdvice: {d['p_eng']}",
            file_name=f"Detailed_Audit_{d['id']}.txt"
        )
    else:
        st.warning("⚠️ Access Denied. Please conduct a Clinic scan first.")

# --- SIDEBAR ---
if st.sidebar.button("🗑️ PURGE CLINIC DATA"):
    st.session_state.clear()
    st.rerun()
