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
# Header
# -----------------------------
st.title("MKT 335 Consumer Behavior Project")
st.subheader("231 West Patisserie")

st.write(
    """
    We are a student team conducting a consumer behavior analysis and
    marketing project for 231 West Patisserie.
    
    Our goal is to better understand customer behavior and use what we learn
    to develop useful marketing recommendations for the business.
    """
)

# -----------------------------
# Our Objective
# -----------------------------
st.header("Our Objective")

st.write(
    """
    We want to better understand the customers of 231 West Patisserie,
    including:
    """
)

st.markdown("""
- Customer demographics
- Customer purchasing behavior
- Customer lifestyles and characteristics
- Patterns between customer characteristics and purchases
""")

st.write(
    """
    We will use this information to develop a consumer profile and create
    marketing recommendations based on concepts from our MKT 335 course.
    """
)

# -----------------------------
# What Data We Need
# -----------------------------
st.header("What Data We Need")

st.write(
    """
    To complete our project, we would like to collect information from
    three main sources:
    """
)

st.subheader("1. Sales Data")

st.markdown("""
- What was purchased
- Amount spent
- Date of the transaction
- Time of the transaction
- If available, information that helps us understand repeat visits
""")

st.subheader("2. Customer Observations")

st.markdown("""
We will make general observations while sitting in the store, such as:

- Approximate age range
- Gender presentation
- General attire
- Other broad, non-identifying characteristics
""")

st.subheader("3. Social Media")

st.markdown("""
We may review publicly available information about the business's social
media audience and engagement.
""")

# -----------------------------
# How We Will Collect the Data
# -----------------------------
st.header("How We Will Collect the Data")

st.write(
    """
    We have created a simple application that allows us to record observations
    and organize them into a dataset.
    
    Each observation will include a timestamp. This allows us to compare
    general customer observations with sales information from the same
    period and identify broader purchasing patterns.
    """
)

# -----------------------------
# Privacy Commitment
# -----------------------------
st.header("Our Privacy Commitment")

st.warning(
    """
    We will NOT collect names, credit card information, phone numbers,
    email addresses, or other personally identifying information.
    """
)

st.write(
    """
    The information we collect will be used only for our MKT 335 class
    project and will be handled responsibly.
    """
)

st.markdown("""
**We will:**

- Use the data only for this project
- Avoid collecting personally identifying information
- Keep our observations focused on broad patterns rather than individual customers
- Use the information to create an overall analysis, not individual customer profiles
""")

# -----------------------------
# What 231 West Patisserie Receives
# -----------------------------
st.header("What 231 West Patisserie Will Receive")

st.write(
    """
    In exchange for allowing us to conduct this project, we will provide
    231 West Patisserie with an executive report at no monetary cost.
    """
)

st.write(
    """
    The report will summarize our findings and provide insights into:

    - Customer characteristics
    - Purchasing patterns
    - Consumer behavior
    - Potential marketing opportunities
    """
)

# -----------------------------
# Closing
# -----------------------------
st.header("Thank You")

st.write(
    """
    We appreciate the opportunity to work with 231 West Patisserie.
    Our goal is to make this project useful to the business while treating
    customer information responsibly.
    """
)

st.divider()

st.caption("MKT 335 · Consumer Behavior Analysis")
