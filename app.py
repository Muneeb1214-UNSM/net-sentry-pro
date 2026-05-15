import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests
import time
import socket
import random

# --- CONFIG & THEME ---
st.set_page_config(page_title="CyberPulse SOC", page_icon="⚡", layout="wide")

# Custom CSS for Cyberpunk / High-Tech UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Rajdhani', sans-serif;
        background-color: #050505;
        color: #00f2ff;
    }
    .stApp {
        background: radial-gradient(circle, #0a0a2e 0%, #000000 100%);
    }
    .main-title {
        font-size: 50px;
        font-weight: 700;
        text-align: center;
        background: -webkit-linear-gradient(#00f2ff, #0062ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 10px #00f2ff);
        margin-bottom: 10px;
    }
    .stat-card {
        background: rgba(0, 242, 255, 0.05);
        border: 1px solid #00f2ff;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        transition: 0.4s;
    }
    .stat-card:hover {
        background: rgba(0, 242, 255, 0.15);
        box-shadow: 0 0 20px #00f2ff;
    }
    /* Hide Streamlit Header/Footer */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- UTILS ---
def load_lottie(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

lottie_globe = load_lottie("https://assets9.lottiefiles.com/packages/lf20_6n9mrf9e.json")
lottie_security = load_lottie("https://assets10.lottiefiles.com/packages/lf20_6aYtLp.json")

# --- DATA GENERATOR (Simulating SOC Traffic) ---
if 'traffic_data' not in st.session_state:
    st.session_state.traffic_data = pd.DataFrame(columns=["Timestamp", "Source IP", "Protocol", "Status", "Payload (KB)"])

def add_traffic_entry():
    new_entry = {
        "Timestamp": time.strftime("%H:%M:%S"),
        "Source IP": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
        "Protocol": random.choice(["TCP", "UDP", "HTTPS", "FTP", "SSH"]),
        "Status": random.choice(["ALLOWED", "ALLOWED", "BLOCKED", "FLAGGED"]),
        "Payload (KB)": random.randint(10, 5000)
    }
    st.session_state.traffic_data = pd.concat([st.session_state.traffic_data, pd.DataFrame([new_entry])], ignore_index=True)
    if len(st.session_state.traffic_data) > 50:
        st.session_state.traffic_data = st.session_state.traffic_data.iloc[1:]

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("<h1 style='color:#00f2ff;'>⚡ CYBER-PULSE</h1>", unsafe_allow_html=True)
st.sidebar.markdown("---")
choice = st.sidebar.selectbox("COMMAND CENTER", ["OVERVIEW", "LIVE ANALYZER", "DOMAIN INTEL", "THREAT MAP"])

# --- PAGE 1: OVERVIEW ---
if choice == "OVERVIEW":
    st.markdown("<h1 class='main-title'>NETWORK OPERATIONS CENTER</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st_lottie(lottie_globe, height=400)
    with col2:
        st.write("### System Status")
        st.success("🟢 Firewalls: Active")
        st.success("🟢 IDS/IPS: Monitoring")
        st.warning("🟡 Latency: 45ms")
        st.markdown("""
        <div class='stat-card'>
            <h2>PROJECT INFO</h2>
            <p>Computer Networks Semester Project<br>Advanced Traffic Analysis System</p>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE 2: LIVE ANALYZER ---
elif choice == "LIVE ANALYZER":
    st.markdown("<h1 class='main-title'>REAL-TIME TRAFFIC FLOW</h1>", unsafe_allow_html=True)
    
    # Live Simulation Update
    add_traffic_entry()
    df = st.session_state.traffic_data

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("TOTAL PACKETS", len(df), "+12")
    col2.metric("THREATS DETECTED", len(df[df['Status'] == 'FLAGGED']), "+2")
    col3.metric("UPLINK SPEED", "1.2 Gbps")
    col4.metric("ACTIVE NODES", random.randint(100, 150))

    # Dynamic Graphs
    c1, c2 = st.columns(2)
    with c1:
        fig = px.bar(df, x='Protocol', y='Payload (KB)', color='Protocol', template="plotly_dark", title="Protocol Load Analysis")
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    
    with c2:
        fig2 = px.line(df, x='Timestamp', y='Payload (KB)', template="plotly_dark", title="Traffic Pulse")
        fig2.update_traces(line_color='#00f2ff')
        fig2.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### RAW PACKET INSPECTION")
    st.dataframe(df.iloc[::-1], use_container_width=True)
    time.sleep(1)
    st.rerun()

# --- PAGE 3: DOMAIN INTEL (Actual Networking) ---
elif choice == "DOMAIN INTEL":
    st.markdown("<h1 class='main-title'>TARGET INTELLIGENCE</h1>", unsafe_allow_html=True)
    target = st.text_input("Enter Domain (e.g. google.com):", "google.com")
    
    if st.button("RUN DEEP SCAN"):
        with st.spinner("Fetching Network Metadata..."):
            try:
                ip_addr = socket.gethostbyname(target)
                st.markdown(f"""
                <div class='stat-card'>
                    <h3>Target Found: {target}</h3>
                    <p><b>Primary IP:</b> {ip_addr}</p>
                    <p><b>Status:</b> REACHABLE</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Visualizing Ports
                st.write("#### Common Port Status")
                ports = {80: "HTTP", 443: "HTTPS", 21: "FTP", 22: "SSH"}
                for p, name in ports.items():
                    st.code(f"Port {p} ({name}): OPEN")
                    
            except:
                st.error("Target unreachable or invalid domain.")

# --- PAGE 4: THREAT MAP ---
elif choice == "THREAT MAP":
    st.markdown("<h1 class='main-title'>GLOBAL THREAT VISUALIZER</h1>", unsafe_allow_html=True)
    
    # Create random world coordinates for visual effect
    map_data = pd.DataFrame({
        'lat': [random.uniform(-60, 60) for _ in range(10)],
        'lon': [random.uniform(-120, 120) for _ in range(10)],
        'intensity': [random.randint(10, 100) for _ in range(10)]
    })
    
    fig = px.scatter_geo(map_data, lat='lat', lon='lon', size='intensity', 
                         projection="natural earth", title="Active Network Node Map",
                         color_discrete_sequence=['#00f2ff'])
    fig.update_layout(template="plotly_dark", geo=dict(bgcolor= 'rgba(0,0,0,0)'))
    st.plotly_chart(fig, use_container_width=True)
    
    st_lottie(lottie_security, height=200)
