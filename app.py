import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
import time
import socket
import random

# --- CONFIG & THEME ---
st.set_page_config(page_title="CyberPulse SOC", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;500;700&display=swap');
    html, body, [class*="css"] { font-family: 'Rajdhani', sans-serif; background-color: #050505; color: #00f2ff; }
    .stApp { background: radial-gradient(circle, #0a0a2e 0%, #000000 100%); }
    .main-title {
        font-size: 50px; font-weight: 700; text-align: center;
        background: -webkit-linear-gradient(#00f2ff, #0062ff);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 10px #00f2ff); margin-bottom: 10px;
    }
    .stat-card {
        background: rgba(0, 242, 255, 0.05); border: 1px solid #00f2ff;
        border-radius: 10px; padding: 20px; text-align: center;
    }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- SAFE LOTTIE LOADING ---
def load_lottie(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Naye aur working Lottie URLs
lottie_globe = load_lottie("https://lottie.host/8553641b-10f7-434a-9524-71e98822588c/OayXwS3S0R.json")
lottie_security = load_lottie("https://lottie.host/68297b69-8088-466d-959c-8a192f1505c2/Wv0k06H4tV.json")

# --- DATA GENERATOR ---
if 'traffic_data' not in st.session_state:
    st.session_state.traffic_data = pd.DataFrame(columns=["Timestamp", "Source IP", "Protocol", "Status", "Payload (KB)"])

def add_traffic_entry():
    new_entry = {
        "Timestamp": time.strftime("%H:%M:%S"),
        "Source IP": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
        "Protocol": random.choice(["TCP", "UDP", "HTTPS", "FTP", "SSH"]),
        "Status": random.choice(["ALLOWED", "BLOCKED", "FLAGGED"]),
        "Payload (KB)": random.randint(10, 5000)
    }
    st.session_state.traffic_data = pd.concat([st.session_state.traffic_data, pd.DataFrame([new_entry])], ignore_index=True)
    if len(st.session_state.traffic_data) > 50:
        st.session_state.traffic_data = st.session_state.traffic_data.iloc[1:]

# --- SIDEBAR ---
st.sidebar.markdown("<h1 style='color:#00f2ff;'>⚡ CYBER-PULSE</h1>", unsafe_allow_html=True)
choice = st.sidebar.selectbox("COMMAND CENTER", ["OVERVIEW", "LIVE ANALYZER", "DOMAIN INTEL", "THREAT MAP"])

# --- PAGE 1: OVERVIEW ---
if choice == "OVERVIEW":
    st.markdown("<h1 class='main-title'>NETWORK OPERATIONS CENTER</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])
    with col1:
        if lottie_globe:
            st_lottie(lottie_globe, height=400, key="globe")
        else:
            st.markdown("<h1 style='text-align:center; font-size:100px;'>🌐</h1>", unsafe_allow_html=True)
    with col2:
        st.write("### System Status")
        st.success("🟢 Firewalls: Active")
        st.success("🟢 IDS/IPS: Monitoring")
        st.markdown("<div class='stat-card'><h2>PROJECT</h2><p>Computer Networks Lab<br>Advanced Analyzer</p></div>", unsafe_allow_html=True)

# --- PAGE 2: LIVE ANALYZER ---
elif choice == "LIVE ANALYZER":
    st.markdown("<h1 class='main-title'>REAL-TIME TRAFFIC FLOW</h1>", unsafe_allow_html=True)
    add_traffic_entry()
    df = st.session_state.traffic_data
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("PACKETS", len(df))
    c2.metric("THREATS", len(df[df['Status'] == 'FLAGGED']))
    c3.metric("UPLINK", "1.2 Gbps")
    c4.metric("NODES", "142")

    c_left, c_right = st.columns(2)
    with c_left:
        fig = px.bar(df, x='Protocol', y='Payload (KB)', color='Protocol', template="plotly_dark")
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    with c_right:
        fig2 = px.line(df, x='Timestamp', y='Payload (KB)', template="plotly_dark")
        fig2.update_traces(line_color='#00f2ff')
        fig2.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(df.iloc[::-1], use_container_width=True)
    time.sleep(1)
    st.rerun()

# --- PAGE 3: DOMAIN INTEL ---
elif choice == "DOMAIN INTEL":
    st.markdown("<h1 class='main-title'>TARGET INTELLIGENCE</h1>", unsafe_allow_html=True)
    target = st.text_input("Enter Domain:", "google.com")
    if st.button("RUN SCAN"):
        try:
            ip = socket.gethostbyname(target)
            st.markdown(f"<div class='stat-card'><h3>IP: {ip}</h3><p>Status: Reachable</p></div>", unsafe_allow_html=True)
        except:
            st.error("Invalid Domain")

# --- PAGE 4: THREAT MAP ---
elif choice == "THREAT MAP":
    st.markdown("<h1 class='main-title'>GLOBAL THREAT MAP</h1>", unsafe_allow_html=True)
    map_data = pd.DataFrame({
        'lat': [random.uniform(-60, 60) for _ in range(10)],
        'lon': [random.uniform(-120, 120) for _ in range(10)],
        'size': [random.randint(10, 100) for _ in range(10)]
    })
    fig = px.scatter_geo(map_data, lat='lat', lon='lon', size='size', projection="natural earth", color_discrete_sequence=['#00f2ff'])
    fig.update_layout(template="plotly_dark", geo=dict(bgcolor= 'rgba(0,0,0,0)'))
    st.plotly_chart(fig, use_container_width=True)
    if lottie_security:
        st_lottie(lottie_security, height=200, key="security")
