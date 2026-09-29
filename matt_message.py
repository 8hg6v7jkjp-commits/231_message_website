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
# Custom Styling
# -----------------------------
st.markdown("""
<style>
    /* Main page */
    .main {
        max-width: 850px;
        margin: auto;
    }

    /* Remove excessive top padding */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    /* Typography */
    h1 {
        font-size: 2.7rem !important;
        font-weight: 700 !important;
        letter-spacing: -1px;
        margin-bottom: 0.25rem;
    }

    h2 {
        font-size: 1.45rem !important;
        font-weight: 650 !important;
        margin-top: 2.5rem !important;
        margin-bottom: 0.8rem !important;
    }

    p, li {
        font-size: 1.02rem;
        line-height: 1.7;
    }

    /* Intro */
    .subtitle {
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
    }

    /* Highlight box */
    .highlight {
        background: #f7f4ef;
        border-left: 4px solid #8b6f47;
        padding: 1.2rem 1.4rem;
        border-radius: 6px;
        margin: 1.2rem 0;
    }

    /* Request cards */
    .data-card {
        background: #fafafa;
        border: 1px solid #e8e8e8;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        margin: 0.7rem 0;
    }

    .data-title {
        font-weight: 650;
        font-size: 1.05rem;
        margin-bottom: 0.35rem;
    }

    .data-description {
        color: #666;
        line-height: 1.5;
    }

    /* Footer */
    .footer {
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid #e5e5e5;
        color: #777;
        font-size: 0.9rem;
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

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="data-card">
        <div class="data-title">Sales Data</div>
        <div class="data-description">
            Purchase and transaction information.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="data-card">
        <div class="data-title">Customer Observations</div>
        <div class="data-description">
            General demographics and attire.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="data-card">
        <div class="data-title">Social Media</div>
        <div class="data-description">
            Information about your audience and engagement.
        </div>
    </div>
    """, unsafe_allow_html=True)

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

st.markdown("""
<div class="highlight">

We understand that this information is sensitive. <strong>Our team will use
the data only for this project and will handle it responsibly.</strong>

We will not collect names, payment information, or other personally
identifying information.

</div>
""", unsafe_allow_html=True)

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