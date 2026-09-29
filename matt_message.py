```python
import streamlit as st

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
# Header
# -----------------------------
st.title("Our Project")

st.markdown(
    '<div class="subtitle">MKT 335 · Consumer Behavior Analysis</div>',
    unsafe_allow_html=True
)

st.markdown("""
We are a student team working on a consumer behavior analysis and marketing
plan for **231 West Patisserie**. Our goal is to apply the concepts we have
learned in class to a real business.
""")


# -----------------------------
# Objective
# -----------------------------
st.header("What Is Our Objective?")

st.write("""
Our objective is to apply consumer behavior concepts to develop a marketing
plan for 231 West Patisserie. To do this, we want to better understand your
customers, including their demographics, lifestyles, and purchasing behavior.
""")

st.write("""
Using the data we collect, we hope to build a profile of your target consumers
and use our consumer behavior knowledge to develop effective marketing
recommendations.
""")


# -----------------------------
# Data Collection
# -----------------------------
st.header("How Will We Achieve Our Objective?")

st.write("""
To build our marketing plan, we need data. We have identified three main
sources of information:
""")

st.subheader("Sales Data")

st.write("Purchase and transaction information.")

st.subheader("Customer Observations")

st.write("General demographics and attire.")

st.subheader("Social Media")

st.write("Information about your audience and engagement.")

st.write("""
We have built an application that allows us to quickly enter observations
into a dataset, making the collection process simple and efficient.
""")


# -----------------------------
# What We Need
# -----------------------------
st.header("What We Need From You")

st.write("We would like to collect sales data including:")

st.markdown("""
- **What was purchased**
- **How much was spent**
- **The date and time of the transaction**
- **If available, information that can help us understand how many times a customer visited**
""")

st.write("""
I will also sit in the store to collect general demographic observations,
such as approximate age, gender, and attire.
""")

st.write("""
Our application records the timestamp of each observation. Then, we
can compare these timestamped demographics data with timestamped sales data to identify broader patterns
between customer characteristics and purchasing behavior.
""")


# -----------------------------
# Data Safety
# -----------------------------
st.header("How Will We Handle the Data?")

st.write("""
We understand that this information is sensitive. **Our team will use
the data only for this project and will handle it responsibly.**
""")

st.write("""
We will not collect names, payment information, or other personally
identifying information.
""")


# -----------------------------
# What They Receive
# -----------------------------
st.header("What Is In It For You?")

st.write("""
In exchange for allowing us to conduct this project, **We will provide an
executive report to 231 West Patisserie at no monetary cost.**
""")

st.write("""
The report will summarize our findings and provide insights into your
customers, purchasing patterns, and potential marketing opportunities.
""")


# -----------------------------
# Footer
# -----------------------------
st.markdown("""
<div class="footer">
    MKT 335 · Consumer Behavior Analysis
</div>
""", unsafe_allow_html=True)
```


st.divider()

st.caption("MKT 335 · Consumer Behavior Analysis")
