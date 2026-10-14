"""
FixitAI — Streamlit demo UI.

Run with:
    streamlit run app/app.py

Responsibilities (scaffold only):
  - Accept resume upload (PDF/DOCX) and JD text input.
  - Run pipeline steps 1–6.
  - Display explanation report and overall score.
  - Show baseline comparison table.
"""

import streamlit as st

st.set_page_config(page_title="FixitAI", layout="wide")

st.title("FixitAI — Resume–JD Compatibility Analyser")
st.caption("Human-aligned, evidence-based scoring framework.")

# TODO: wire up pipeline steps 1–6
# TODO: add baseline comparison section
# TODO: add gap analysis and fairness probe toggles

st.info("Pipeline not yet implemented. Scaffold only.")
