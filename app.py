# OMEGA v4.0 - Web App
import streamlit as st
import pandas as pd
import numpy as np
import sys
sys.path.insert(0, '.')
from omega_v4 import OMEGA, PHOENIX, TITAN, NEXUS

st.set_page_config(page_title="OMEGA v4.0", page_icon="⚡", layout="wide")
st.title("⚡ OMEGA v4.0")
st.subheader("Hybrid Autonomous Intelligence | Architect: Owoicho Emmanuel")

uploaded = st.file_uploader("Upload your CSV", type=["csv"])
if uploaded:
    data = pd.read_csv(uploaded)
    st.write("Preview:", data.head())
    cleaned = PHOENIX.run(data)
    target = st.selectbox("Choose target column", cleaned.columns)
    if st.button("Run OMEGA"):
        model, metrics = TITAN.run(cleaned, target)
        st.success(f"Best Model: {metrics['Best_Model']} | R2: {metrics['R2']:.4f}")
        st.json(metrics)
        st.info(NEXUS.run(metrics))
else:
    st.info("Upload a CSV to start. Or click below for demo.")
    if st.button("Run Demo"):
        report = OMEGA.run()
        st.json(report["metrics"])
        st.success(report["decision"])
