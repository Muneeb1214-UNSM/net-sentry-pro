 import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_lottie import st_lottie
import requests
import time
import random

# --- SETTING UP MODERN THEME ---
st.set_page_config(page_title="NetGuard AI", layout="wide", page_icon="🛡️")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0e1117; color: white; }
    .status-card {
        background: #161b22; border-radius: 15px; padding: 20px;
        border: 1px solid #30363d; margin-bottom: 20px;
    }
    .score-high { color: #238636; font-size: 40px; font-weight: bold; }
    .score-low { color: #da3633; font-size: 40px; font-weight: bold; }
    header {visibility: hidden;} footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- LOAD ASSETS ---
def load_lottie(url):
    try: return requests.get(url).json()
    except: return None

lottie_secure = load_lottie("https://lottie.host/8553641b-10f7-434a-9524-71e98822588c/OayXwS3S0R.json")

# --- DATA SIMULATION ENGINE ---
def get_device_data():
    devices = [
        {"Device": "Smart TV", "IP": "192.168.1.10", "Activity": "Streaming", "Risk": "Low", "Data_Sent": "1.2 GB"},
        {"Device": "CCTV Camera", "IP": "192.168.1.15", "Activity": "Uploading to Unknown Server", "Risk": "High", "Data_Sent": "450 MB"},
        {"Device": "iPhone 15", "IP": "192.168.1.5", "Activity": "Browsing", "Risk": "Low", "Data_Sent": "80 MB"},
        {"Device": "Smart Fridge", "IP": "192.168.1.20", "Activity": "Idle", "Risk": "Medium", "Data_Sent": "5 MB"}
    ]
    return pd.DataFrame(devices)

# --- AI ADVISOR LOGIC ---
def get_ai_advice(score):
    if score > 80:
        return "✅ Aapka Network safe hai. Tamam devices sahi kaam kar rahe hain."
    elif score > 50:
        return "⚠️ Kuch devices (CCTV/Fridge) zyada data bhej rahe hain. Unki settings check karein."
    else:
        return "🚨 Khatra! Aapka privacy score bohot kam hai. Kisi ne unauthorized access kiya hai."

# --- NAVIGATION ---
st.sidebar.title("🛡️ NetGuard AI")
menu = st.sidebar.radio("Navigation", ["Home Dashboard", "Privacy Scan", "AI Assistant"])

if menu == "Home Dashboard":
    st.markdown("<h1 style='text-align:center;'>NetGuard AI Guardian</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    # Calculate Score
    privacy_score = random.randint(45, 95)
    
    with col1:
        st.markdown("<div class='status-card'>", unsafe_allow_html=True)
        st.write("### Network Health")
        if privacy_score > 70:
            st.markdown(f"<p class='score-high'>{privacy_score}%</p>", unsafe_allow_html=True)
            st.write("Status: Secure")
        else:
            st.markdown(f"<p class='score-low'>{privacy_score}%</p>", unsafe_allow_html=True)
            st.write("Status: Warning")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        if lottie_secure: st_lottie(lottie_secure, height=150)
    
    with col3:
        st.markdown("<div class='status-card'>", unsafe_allow_html=True)
        st.write("### AI Summary")
        st.info(get_ai_advice(privacy_score))
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("### Active Devices on your Wi-Fi")
    df = get_device_data()
    st.table(df)

    # Traffic Graph
    st.write("### Data Usage Trend")
    fig = px.bar(df, x='Device', y='Data_Sent', color='Risk', template="plotly_dark",
                 color_discrete_map={"Low": "#238636", "Medium": "#e3b341", "High": "#da3633"})
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Privacy Scan":
    st.header("Deep Privacy Inspection")
    if st.button("Start Deep Scan"):
        with st.spinner("Analyzing Packet Patterns..."):
            time.sleep(3)
            st.warning("Detection: CCTV Camera is sending unencrypted packets to a server in Russia.")
            st.error("Action Required: Block IP 45.12.11.0 on your router.")
            st.image("https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=SecurityScanComplete")

elif menu == "AI Assistant":
    st.header("Ask NetGuard AI")
    user_input = st.text_input("Ask anything (e.g. Is my Wi-Fi safe?)")
    if user_input:
        st.write("🤖 **AI Agent:** Aapka Smart TV filhal Amazon servers se connect hai jo ke normal hai. Lekin aapka CCTV camera suspicious behavior dikha raha hai. Kya aap usay block karna chahte hain?")
