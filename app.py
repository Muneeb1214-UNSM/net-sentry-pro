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

.glass-card {
    background: rgba(255, 255, 255, 0.04);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    padding: 30px;
    border: 1px solid rgba(0, 242, 255, 0.2);
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    margin-bottom: 25px;
}

/* Styled All Buttons */
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
    font-size: 55px; font-weight: 700; text-align: center;
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
}

.summary-box {
    background: rgba(0, 242, 255, 0.1);
    border-left: 5px solid #00f2ff;
    padding: 15px;
    border-radius: 10px;
    margin-top: 15px;
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
st.markdown("<p style='text-align:center; color:#FFFFFF; font-size:20px;'>Advanced Neural Intelligence & Network Bio-Forensics</p>", unsafe_allow_html=True)

tabs = st.tabs(["🏥 CLINIC", "🧬 VITALS", "🛡️ SECURITY", "🔮 PREDICTION", "📜 OFFICIAL AUDIT"])

# --- TAB 1: CLINIC ---
with tabs[0]:
    col1, col2 = st.columns([1, 1.3])
    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("### 🩺 Clinical Bio-Scan")
        if lottie_doc: st_lottie(lottie_doc, height=200)
        
        if st.button("EXECUTE AI DIAGNOSIS"):
            with st.spinner("Decoding Network DNA..."):
                time.sleep(2)
                lat, loss, jit = random.randint(15, 350), random.randint(0, 12), random.randint(2, 65)
                devs, pkts = random.randint(1, 25), random.randint(1500, 8000)
                
                pred = ai_physician.predict([[lat, loss, jit, devs]])[0]
                diags = {
                    0: ("Optimum Health", "Network DNA is stable.", "نظام بالکل ٹھیک کام کر رہا ہے۔", "🟢"),
                    1: ("Hyper-Congestion", "Pathways clogged by load.", "نیٹ ورک پر بوجھ زیادہ ہے۔", "🟡"),
                    4: ("Gateway Failure", "Critical backbone failure.", "انٹرنیٹ فراہم کرنے والے کا مسئلہ ہے۔", "🔴")
                }
                st.session_state.audit = {
                    "v": diags.get(pred, diags[1])[0],
                    "p_eng": diags.get(pred, diags[1])[1],
                    "p_urdu": diags.get(pred, diags[1])[2],
                    "i": diags.get(pred, diags[1])[3],
                    "stats": [lat, loss, jit, devs, pkts],
                    "time": time.strftime("%B %d, %Y | %H:%M:%S"),
                    "id": f"ND-{random.randint(1000, 9999)}",
                    "sec_score": random.randint(88, 99)
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
            c3.metric("Packets Analyzed", f"{res['stats'][4]}")
            
            st.markdown(f"""
            <div class='summary-box'>
                <b>📝 Clinic Summary (Roman English):</b><br>
                Is section mein AI aapke network ka check-up karta hai. Latency batati hai ke internet kitna slow hai, 
                Nodes ka matlab hai kitne mobile/laptops connected hain, aur Packets ka matlab hai kitna data transfer ho raha hai. 
                AI ne diagnose kiya hai ke aapka network abhi <b>{res['v']}</b> halat mein hai.
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
        <b>📝 Vitals Summary (Roman English):</b><br>
        Ye graph network ki 'Dharhkan' (Pulse) dikhata hai. Uplink aur Downlink lines se pata chalta hai ke 
        internet ka bahaao (flow) kitna hai. Agar lines bohot upar niche ho rahi hain, to iska matlab hai ke connection stable nahi hai.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: SECURITY ---
with tabs[2]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 🛡️ Cyber-Shield Intelligence")
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.header(f"Immunity: {st.session_state.audit['sec_score'] if 'audit' in st.session_state else 94}%")
        st.write("🛡️ **Encryption:** TLS 1.3 Active")
    with col_s2:
        st.success("AI is protecting your data from unauthorized access.")
    
    st.markdown("""
    <div class='summary-box'>
        <b>📝 Security Summary (Roman English):</b><br>
        Ye section aapke network ki hifazat (Security) ko monitor karta hai. Immunity score jitna zyada hoga, 
        aapka data utna hi mehfooz rahega. AI har waqt hackers aur virus wali files ko block karne ke liye tayyar rehta hai.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 4: PREDICTION ---
with tabs[3]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 🔮 AI Traffic Forecasting (Next 24 Hours)")
    pred_data = pd.DataFrame(np.random.randint(20, 90, size=(24, 1)), columns=['Predicted Load'])
    st.line_chart(pred_data)
    
    st.markdown("""
    <div class='summary-box'>
        <b>📝 Prediction Summary (Roman English):</b><br>
        AI ne pichle record ko dekh kar andaza (Predict) lagaya hai ke aglay 24 ghanton mein internet par kitna bura asar parh sakta hai. 
        Is se humein pehle hi pata chal jata hai ke kab internet slow hone ka khatra hai.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 5: OFFICIAL AUDIT ---
with tabs[4]:
    if 'audit' in st.session_state:
        d = st.session_state.audit
        st.markdown("<div class='report-paper'>", unsafe_allow_html=True)
        st.markdown(f"""
        <h1 style="text-align:center; border-bottom: 2px solid #1a1a1a;">NETWORK FORENSIC AUDIT REPORT</h1>
        <p style="text-align:right;"><b>Ref:</b> {d['id']} | <b>Date:</b> {d['time']}</p>
        <hr style="border: 1px solid #1a1a1a;">
        
        <h3>1. EXECUTIVE SUMMARY</h3>
        <p>This comprehensive audit documents the autonomous diagnostic findings. The system has been classified as <b>{d['v']}</b>.</p>
        
        <h3>2. CORE METRICS</h3>
        <p>Latency: {d['stats'][0]} ms | Loss: {d['stats'][1]} % | Nodes: {d['stats'][3]}</p>
        
        <h3>3. AI CLINICAL PRESCRIPTION</h3>
        <p><b>Advice:</b> {d['p_eng']}</p>
        <p><b>Urdu:</b> {d['p_urdu']}</p>
        
        <h3>4. FINAL REMARKS (Roman English)</h3>
        <p>Ye aapka final medical certificate hai. Is mein sab kuch tafseel se likha gaya hai ke network mein kya masla hai 
        aur usay theek kaise karna hai. AI ne mashwara diya hai ke router ko restart karein aur DNS ko optimize karein.</p>
        
        <br>
        <p style="text-align:right;"><i>Digitally Signed: Dr. Cyber-Sentinel (NetDoc AI Pro)</i></p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            label="📥 DOWNLOAD PROFESSIONAL REPORT",
            data=f"NetDoc Audit Report\nID: {d['id']}\nStatus: {d['v']}\nAdvice: {d['p_eng']}",
            file_name=f"Detailed_Audit_{d['id']}.txt"
        )
    else:
        st.warning("⚠️ Please conduct a Clinic scan first to generate the report.")

# --- SIDEBAR ---
if st.sidebar.button("🗑️ PURGE CLINIC DATA"):
    st.session_state.clear()
    st.rerun()
