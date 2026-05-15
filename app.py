import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
import random
from streamlit_lottie import st_lottie
import requests

# --- FUTURISTIC CONFIG ---
st.set_page_config(page_title="VortexAI Forensics", layout="wide", page_icon="🌀")

# --- ULTRA-MODERN CSS (Cyber-Terminal Look) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;500&display=swap');
    .stApp { background: #020205; color: #00e5ff; font-family: 'Fira Code', monospace; }
    .terminal-card {
        border-left: 5px solid #ff0055; background: rgba(255, 0, 85, 0.02);
        padding: 20px; border-radius: 5px; margin-bottom: 15px;
    }
    .ai-commander {
        border: 1px solid #00e5ff; background: rgba(0, 229, 255, 0.05);
        padding: 20px; border-radius: 20px; box-shadow: 0 0 20px rgba(0, 229, 255, 0.2);
    }
    .glitch-text { color: #ff0055; font-weight: bold; text-transform: uppercase; }
    header {visibility: hidden;} footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- ASSETS ---
def load_lottie(url):
    try: return requests.get(url, timeout=5).json()
    except: return None

lottie_core = load_lottie("https://lottie.host/8553641b-10f7-434a-9524-71e98822588c/OayXwS3S0R.json")

# --- AI INCIDENT COMMANDER LOGIC ---
def ai_incident_commander(threat_level):
    comments = {
        "LOW": [
            "Officer, the network is stable. All nodes are reporting green.",
            "Minimal packet fragmentation detected. System health is optimal."
        ],
        "MEDIUM": [
            "Alert! Unusual handshake patterns detected on Node 192.168.4.1.",
            "Warning: Port 443 is receiving high-entropy payloads. Investigation advised."
        ],
        "HIGH": [
            "CRITICAL: Unauthorized privilege escalation attempt detected!",
            "EMERGENCY: DDoS flood in progress. Autonomous containment engaged."
        ]
    }
    return random.choice(comments[threat_level])

# --- SIMULATED FORENSIC DATA ---
if 'forensic_logs' not in st.session_state:
    st.session_state.forensic_logs = []

def generate_forensic_event():
    threats = ["CLEAN", "CLEAN", "SCAN", "EXFIL", "DDoS"]
    t = random.choice(threats)
    level = "LOW" if t == "CLEAN" else "MEDIUM" if t == "SCAN" else "HIGH"
    
    event = {
        "Timestamp": time.strftime("%H:%M:%S"),
        "Event": t,
        "Threat_Level": level,
        "Origin": f"ZONE-{random.randint(1,9)}",
        "Data_Volume": random.randint(100, 5000)
    }
    st.session_state.forensic_logs.append(event)
    if len(st.session_state.forensic_logs) > 15: st.session_state.forensic_logs.pop(0)
    return level

# --- APP LAYOUT ---
st.markdown("<h1 style='text-align:center; color:#ff0055;'>VORTEX-AI // NEURAL FORENSICS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00e5ff;'>Advanced Network Attack Path Reconstruction Tool</p>", unsafe_allow_html=True)

# Main Grid
col_a, col_b = st.columns([1, 2])

with col_a:
    st.markdown("<div class='ai-commander'>", unsafe_allow_html=True)
    st.write("### 🤖 INCIDENT COMMANDER")
    if lottie_core: st_lottie(lottie_core, height=180)
    
    # Generate event and get threat level
    current_level = generate_forensic_event()
    st.write(f"**AI VERDICT:** {current_level}")
    st.info(ai_incident_commander(current_level))
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 3D Visual Metric
    st.write("#### Neural Load")
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = random.randint(20, 95) if current_level != "HIGH" else 99,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Traffic Intensity", 'font': {'color': "#00e5ff"}},
        gauge = {'axis': {'range': [None, 100], 'tickcolor': "#00e5ff"},
                 'bar': {'color': "#ff0055"},
                 'bgcolor': "black",
                 'borderwidth': 2,
                 'bordercolor': "#00e5ff"}
    ))
    fig_gauge.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "#00e5ff", 'family': "Fira Code"})
    st.plotly_chart(fig_gauge, use_container_width=True)

with col_b:
    st.write("### 🌐 3D ATTACK PATH RECONSTRUCTION")
    
    # Create 3D Scatter for Traffic
    df = pd.DataFrame(st.session_state.forensic_logs)
    if not df.empty:
        # Simulate 3D coordinates
        df['x'] = [random.uniform(0, 10) for _ in range(len(df))]
        df['y'] = [random.uniform(0, 10) for _ in range(len(df))]
        df['z'] = df['Data_Volume'] / 100
        
        fig_3d = px.scatter_3d(df, x='x', y='y', z='z', color='Threat_Level',
                              text='Event', size='Data_Volume',
                              color_discrete_map={"LOW": "#00ffcc", "MEDIUM": "#ffcc00", "HIGH": "#ff0055"})
        fig_3d.update_layout(scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(title="Volume")),
                             paper_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig_3d, use_container_width=True)
    
    # Forensic Timeline Table
    st.write("### 📜 FORENSIC TIMELINE")
    for log in reversed(st.session_state.forensic_logs):
        color = "#00ffcc" if log['Threat_Level'] == "LOW" else "#ff0055"
        st.markdown(f"""
        <div class='terminal-card' style='border-left: 5px solid {color};'>
            <span style='color:gray;'>[{log['Timestamp']}]</span> 
            <b>EVENT: {log['Event']}</b> // ORIGIN: {log['Origin']} // 
            STATUS: <span style='color:{color};'>{log['Threat_Level']}</span>
        </div>
        """, unsafe_allow_html=True)

# Footer info
st.sidebar.title("VORTEX CORE")
st.sidebar.write("Project: VortexAI Forensics")
st.sidebar.write("Module: Neural Path Recon")
if st.sidebar.button("RESET CORE"):
    st.session_state.forensic_logs = []
    st.rerun()

time.sleep(2)
st.rerun()
