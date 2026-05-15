import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests
import time
import random

# --- MODERN UI SETUP ---
st.set_page_config(page_title="AI-QoS Optimizer", layout="wide", page_icon="⚡")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');
    html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; background-color: #040911; color: #e0e0e0; }
    .stApp { background: radial-gradient(circle, #0a192f 0%, #040911 100%); }
    .status-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(0, 255, 255, 0.2);
        border-radius: 15px; padding: 25px; backdrop-filter: blur(10px);
    }
    .neon-text { color: #00f2ff; text-shadow: 0 0 10px #00f2ff; }
    header {visibility: hidden;} footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- LOAD ASSETS ---
def load_lottie(url):
    try: return requests.get(url, timeout=5).json()
    except: return None

lottie_speed = load_lottie("https://lottie.host/8553641b-10f7-434a-9524-71e98822588c/OayXwS3S0R.json")

# --- AI QoS ENGINE (Simulation) ---
if 'qos_history' not in st.session_state:
    st.session_state.qos_history = pd.DataFrame(columns=["Time", "Activity", "Priority", "Latency", "Bandwidth"])

def run_ai_optimizer(mode):
    activities = ["Gaming", "Video Call", "Netflix", "File Download", "Web Browsing"]
    current_act = random.choice(activities) if mode == "Auto" else mode
    
    # AI Logic: Assign priority and simulate latency/bandwidth
    if current_act in ["Gaming", "Video Call"]:
        priority = "Critical"
        latency = random.randint(10, 30)
        bw = random.randint(70, 95) # High bandwidth allocation
    elif current_act == "Netflix":
        priority = "Medium"
        latency = random.randint(40, 80)
        bw = random.randint(50, 70)
    else:
        priority = "Low"
        latency = random.randint(100, 250)
        bw = random.randint(10, 40)

    new_data = {
        "Time": time.strftime("%H:%M:%S"),
        "Activity": current_act,
        "Priority": priority,
        "Latency": latency,
        "Bandwidth": bw
    }
    st.session_state.qos_history = pd.concat([st.session_state.qos_history, pd.DataFrame([new_data])], ignore_index=True)
    if len(st.session_state.qos_history) > 20:
        st.session_state.qos_history = st.session_state.qos_history.iloc[1:]
    return new_data

# --- APP LAYOUT ---
st.markdown("<h1 class='neon-text' style='text-align:center;'>AI-POWERED QoS OPTIMIZER</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Smart Bandwidth Allocation & Network Latency Control</p>", unsafe_allow_html=True)

# Dashboard Control
st.sidebar.title("⚡ QoS CONTROL")
mode_select = st.sidebar.selectbox("Optimization Mode", ["Auto-AI", "Gaming Mode", "Work Mode (Meeting)", "Power Saver"])

st.sidebar.markdown("---")
st.sidebar.write("### AI Agent Status")
st.sidebar.success("🟢 Agent Online")
st.sidebar.info("AI is dynamically analyzing packet bursts to reduce jitter.")

# Main Screen
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("<div class='status-card'>", unsafe_allow_html=True)
    st.write("### AI Agent Insights")
    if lottie_speed: st_lottie(lottie_speed, height=200)
    
    # Process AI Logic
    current_mode = mode_select.split(" ")[0] if "Mode" in mode_select else "Auto"
    current_stats = run_ai_optimizer(current_mode)
    
    st.write(f"**Detecting:** {current_stats['Activity']}")
    st.write(f"**AI Priority:** {current_stats['Priority']}")
    
    # Gauge Chart for Latency
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = current_stats['Latency'],
        title = {'text': "Latency (ms)"},
        gauge = {'axis': {'range': [None, 300]},
                 'bar': {'color': "#00f2ff"},
                 'steps': [
                     {'range': [0, 50], 'color': "green"},
                     {'range': [50, 150], 'color': "yellow"},
                     {'range': [150, 300], 'color': "red"}]}
    ))
    fig_gauge.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"}, height=250)
    st.plotly_chart(fig_gauge, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='status-card'>", unsafe_allow_html=True)
    st.write("### Bandwidth Allocation (AI Optimized)")
    
    hist_df = st.session_state.qos_history
    fig_line = px.line(hist_df, x="Time", y="Bandwidth", color="Priority", 
                       title="Live Bandwidth Distribution", template="plotly_dark")
    fig_line.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_line, use_container_width=True)
    
    st.write("### Real-time Agent Logs")
    st.table(hist_df.tail(5))
    st.markdown("</div>", unsafe_allow_html=True)

# Explainable AI Section
st.markdown("---")
exp_col1, exp_col2 = st.columns(2)
with exp_col1:
    st.write("### 🧠 How AI Optimizes?")
    st.write("""
    1. **Traffic Identification:** AI packets ki 'burstiness' aur 'size' dekh kar activity pehchanta hai.
    2. **Dynamic Queuing:** Gaming packets ko priority queue mein dalta hai taake delay kam ho.
    3. **Resource Throttling:** Background downloads ko temporarily slow karta hai taake video call na rukay.
    """)
with exp_col2:
    st.write("### 📈 Network Health")
    st.progress(random.randint(85, 100))
    st.write("Current Optimization Efficiency: **94.2%**")

# Auto-refresh
time.sleep(2)
st.rerun()
