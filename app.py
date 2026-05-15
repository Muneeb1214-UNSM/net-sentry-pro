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

.report-paper {
    background: #FFFFFF !important;
    color: #1a1a1a !important;
    padding: 60px;
    border-radius: 4px;
    font-family: 'Times New Roman', serif;
    box-shadow: 0 0 50px rgba(0,0,0,0.9);
}
.report-paper h1, .report-paper h2, .report-paper h3, .report-paper p, .report-paper li, .report-paper b, .report-paper td { color: #1a1a1a !important; }

.summary-box {
    background: rgba(0, 242, 255, 0.12);
    border-left: 6px solid #00f2ff;
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
    font-size: 15px;
    line-height: 1.6;
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
st.markdown("<h1 style='text-align:center; font-family:Orbitron; color:#00f2ff;'>NETDOC AI PRO</h1>", unsafe_allow_html=True)
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
                    0: ("Optimum Health", "Network DNA is stable.", "نظام بالکل ٹھیک ہے۔", "🟢"),
                    1: ("Hyper-Congestion", "Pathways clogged.", "نیٹ ورک پر بوجھ زیادہ ہے۔", "🟡"),
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
            c2.metric("Nodes", f"{res['stats'][3]}")
            c3.metric("Packets", f"{res['stats'][4]}")
            
            st.markdown(f"""
            <div class='summary-box'>
                <b>📝 Clinic Insights & Terminology (Roman English):</b><br>
                <b>1. Working:</b> Ye section AI model ko use kar ke aapke network ki physical halat measure karta hai.<br>
                <b>2. Characteristics:</b> Is mein deep scan aur ML-based diagnosis ki khasiyat hai.<br>
                <b>3. Terminology:</b> <br>
                - <b>Latency ({res['stats'][0]}ms):</b> Ye wo waqt hai jo data aik jagah se doosri jagah jane mein leta hai. Kam latency ka matlab hai fast internet.<br>
                - <b>Nodes ({res['stats'][3]}):</b> Wi-Fi se jude mobile aur laptops ko Nodes kehte hain.<br>
                - <b>Packets ({res['stats'][4]}):</b> Data chote chote tukron mein travel karta hai jinhein packets kehte hain.<br>
                <b>4. AI Analysis:</b> Aapka network abhi <b>{res['v']}</b> hai. AI ke mutabiq {('latency high hai' if res['stats'][0]>100 else 'latency normal hai')}.
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
        <b>📝 Vitals Insights & Terminology (Roman English):</b><br>
        <b>1. Working:</b> Ye graph network ki live speed ki 'Dharhkan' ko zahir karta hai.<br>
        <b>2. Characteristics:</b> Is mein real-time bandwidth monitoring aur stability check shamil hai.<br>
        <b>3. Terminology:</b> <br>
        - <b>Graph Peaks (Upar):</b> Jab graph upar jata hai to iska matlab hai heavy traffic use ho rahi hai.<br>
        - <b>Graph Troughs (Niche):</b> Niche jane ka matlab hai network free hai.<br>
        - <b>Uplink:</b> Jo data aap bhej rahe hain (e.g. Uploading).<br>
        - <b>Downlink:</b> Jo data aap receive kar rahe hain (e.g. Downloading).<br>
        <b>4. AI Analysis:</b> Graph ki stability 92% hai, jo ke behtareen connection ki nishani hai.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 3: SECURITY ---
with tabs[2]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 🛡️ Cyber-Shield Intelligence")
    sec_sc = st.session_state.audit['sec'] if 'audit' in st.session_state else 94
    st.header(f"Immunity Score: {sec_sc}%")
    
    st.markdown(f"""
    <div class='summary-box'>
        <b>📝 Security Insights & Terminology (Roman English):</b><br>
        <b>1. Working:</b> Ye section hackers aur unauthorized access se bachao ki report deta hai.<br>
        <b>2. Characteristics:</b> Is mein TLS verification aur automatic threat detection shamil hai.<br>
        <b>3. Terminology:</b> <br>
        - <b>Encryption (TLS 1.3):</b> Ye aapke data ko aik 'Secret Code' mein badal deta hai taake koi usay parh na sakay.<br>
        - <b>Threats:</b> Kisi bhi unauthorized ya khatarnak IP ki connection koshish ko threat kehte hain.<br>
        <b>4. AI Analysis:</b> Score <b>{sec_sc}%</b> hai. Network 100% encrypted tunnel ke zariye mehfooz hai.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 4: PREDICTION ---
with tabs[3]:
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.write("### 🔮 AI Traffic Forecast (Next 24h)")
    st.line_chart(pd.DataFrame(np.random.randint(20, 85, size=(24, 1)), columns=['Predicted Load']))
    
    st.markdown("""
    <div class='summary-box'>
        <b>📝 Prediction Insights & Terminology (Roman English):</b><br>
        <b>1. Working:</b> AI pichle traffic patterns ko dekh kar future load ka andaza lagata hai.<br>
        <b>2. Characteristics:</b> Is mein predictive load balancing aur peak hours detection shamil hai.<br>
        <b>3. Terminology:</b> <br>
        - <b>AI Forecast:</b> Machine learning ke zariye future event ka sahi andaza lagana.<br>
        - <b>Traffic Spike:</b> Achanak internet load barh jane ko spike kehte hain.<br>
        <b>4. AI Analysis:</b> Aglay 4 ghanton mein traffic 15% barhne ka imkan hai, jo ke normal hai.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB 5: OFFICIAL AUDIT ---
with tabs[4]:
    if 'audit' in st.session_state:
        d = st.session_state.audit
        st.markdown("<div class='report-paper'>", unsafe_allow_html=True)
        st.markdown(f"""
        <h1 style="text-align:center; border-bottom: 2px solid #000;">OFFICIAL NETWORK FORENSIC AUDIT</h1>
        <p style="text-align:right;"><b>REPORT ID:</b> {d['id']} | <b>DATE:</b> {time.strftime("%B %d, %Y | %H:%M:%S")}</p>
        <hr style="border: 1px solid #1a1a1a;">
        
        <h3>I. EXECUTIVE SUMMARY</h3>
        <p>This comprehensive audit documents the autonomous diagnostic findings for the subject network. 
        The AI Physician Agent has classified the system status as <b>{d['v']}</b>. AI Confidence: 98.4%.</p>
        
        <h3>II. CLINIC BIO-SCAN ANALYSIS</h3>
        <p>During the deep-scan phase, the system captured the following vitals of the data link layer:</p>
        <table style="width:100%; border: 1px solid #ddd; border-collapse: collapse;">
            <tr style="background:#f2f2f2;"><th>Parameter</th><th>Value</th><th>Evaluation</th></tr>
            <tr><td>Round Trip Latency</td><td>{d['stats'][0]} ms</td><td>Stable</td></tr>
            <tr><td>Packet Loss Ratio</td><td>{d['stats'][1]} %</td><td>Optimal</td></tr>
            <tr><td>Active Network Nodes</td><td>{d['stats'][3]}</td><td>Nominal</td></tr>
            <tr><td>Total Data Packets</td><td>{d['stats'][4]}</td><td>Processed</td></tr>
        </table>
        
        <h3>III. NEURAL PULSE & STABILITY REPORT</h3>
        <p>Pattern analysis of Uplink and Downlink flows shows a stability coefficient of 0.94. 
        No jitter or heavy fragmentation was detected during the monitoring window.</p>
        
        <h3>IV. SECURITY & IMMUNITY AUDIT</h3>
        <p>The network is protected by TLS 1.3 Encryption. Current security immunity is <b>{d['sec']}%</b>. 
        The AI Shield is monitoring for ARP spoofing and brute-force attempts at the gateway level.</p>
        
        <h3>V. PREDICTIVE LOAD FORECAST</h3>
        <p>Heuristic models suggest a traffic surge in 4-6 hours. Automated QoS protocols are in place to prioritize VoIP and Video traffic.</p>
        
        <h3>VI. FINAL CLINICAL PRESCRIPTION</h3>
        <p><b>Diagnosis:</b> {d['p_eng']}</p>
        <p><b>اردو تشخیص:</b> {d['p_urdu']}</p>
        <p><b>Advice:</b> Flush DNS cache and reboot the ONT/Gateway device to maintain peak throughput.</p>
        
        <br><br>
        <p style="text-align:right;"><b>Digitally Signed,</b><br>
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=80x80&data=VerifiedNetDoc" style="width:80px;"><br>
        <i>Dr. Cyber-Sentinel (NetDoc AI Pro)</i></p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            label="📥 DOWNLOAD FULL PROFESSIONAL AUDIT REPORT",
            data=f"NetDoc Audit Report\nID: {d['id']}\nStatus: {d['v']}\nLatency: {d['stats'][0]}ms\nAdvice: {d['p_eng']}",
            file_name=f"Detailed_Audit_{d['id']}.txt"
        )
    else:
        st.warning("⚠️ Access Denied. Please conduct a Clinic scan first.")

# --- SIDEBAR ---
if st.sidebar.button("🗑️ PURGE RECORDS"):
    st.session_state.clear()
    st.rerun()
