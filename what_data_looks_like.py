import streamlit as st
import pandas as pd


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="231 West Patisserie | MKT 335 Project",
    page_icon="🥐",
    layout="centered",
)

# -----------------------------
# Simple Styling
# -----------------------------
st.markdown("""
<style>
    .block-container {
        max-width: 850px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    h1 {
        font-size: 2.5rem !important;
    }

    h2 {
        margin-top: 2rem !important;
    }

    p, li {
        font-size: 1rem;
        line-height: 1.6;
    }

    .subtitle {
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .footer {
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #ddd;
        color: #777;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Data
# -----------------------------
st.title("Sample data")

st.write("The data I collect will be stored in a csv file")

st.write("customer_id,date,time,day,age,sex,attire")

st.write("1,2026-09-30,10:31,Wednesday,40-49,female,casual_other")

# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<div class="footer">
    MKT 335 · Consumer Behavior Analysis
</div>
""", unsafe_allow_html=True)