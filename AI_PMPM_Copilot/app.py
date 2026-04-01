import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="AI-Assisted PMPM Review Copilot", layout="wide")

st.title("AI-Assisted PMPM Review Copilot")
st.write("Connecticut 2008-2009 PMPM summary review")

st.info(
    "The raw market PMPM trend appears negative, but stable-cohort and risk-adjusted results "
    "suggest underlying cost growth. The main signals point to outpatient/carrier growth and "
    "increased ER utilization."
)

# Load summary data
df = pd.read_csv("PMPM_Summary_CT0809.csv", header=None, names=["Metric", "Value"])

# Turn into dictionary
summary = dict(zip(df["Metric"], df["Value"]))

# Define memo
memo_text = f"""
## Executive Summary
The Connecticut market showed a raw PMPM trend of {summary.get('Raw_Trend', 'N/A')} from 2008 to 2009. However, this decline masked a {summary.get('Stable_Trend', 'N/A')} increase in PMPM among members with stable 12-month coverage and a {summary.get('RiskAdj_Trend', 'N/A')} risk-adjusted trend. Taken together, the results suggest underlying medical cost growth despite the apparent market-level decline.

## QA / Interpretation Warning
{summary.get('QA_Flag', 'No QA flag provided.')}

## Key Trend Drivers
Within the stable cohort, the largest increases were observed in Carrier ({summary.get('Car_Growth', 'N/A')}) and Outpatient ({summary.get('OP_Growth', 'N/A')}) spend, while Inpatient spend declined ({summary.get('IP_Growth', 'N/A')}). ER visits per member increased {summary.get('ER_Growth', 'N/A')}, compared with only {summary.get('Amb_Growth', 'N/A')} growth in ambulance trips per member.

## Recommended Follow-Up
- {summary.get('Rec1', 'No recommendation provided.')}
- {summary.get('Rec2', 'No recommendation provided.')}
"""

st.subheader("Trend Comparison")

# Top metrics
col1, col2, col3 = st.columns(3)

col1.metric("Raw Trend", summary.get("Raw_Trend", "N/A"))
col2.metric("Stable Cohort Trend", summary.get("Stable_Trend", "N/A"))
col3.metric("Risk-Adjusted Trend", summary.get("RiskAdj_Trend", "N/A"))

st.subheader("Service-Line Growth")
col4, col5, col6 = st.columns(3)
col4.metric("Carrier Growth", summary.get("Car_Growth", "N/A"))
col5.metric("IP Growth", summary.get("IP_Growth", "N/A"))
col6.metric("OP Growth", summary.get("OP_Growth", "N/A"))


st.subheader("Utilization Follow-Up")
col7, col8 = st.columns(2)
col7.metric("ER Growth", summary.get("ER_Growth", "N/A"))
col8.metric("Ambulance Growth", summary.get("Amb_Growth", "N/A"))

st.subheader("QA Flag")
st.warning(summary.get("QA_Flag", "No QA flag provided."))

st.subheader("Recommended Follow-Up")
st.write(f"- {summary.get('Rec1', 'No recommendation provided.')}")
st.write(f"- {summary.get('Rec2', 'No recommendation provided.')}")

st.subheader("Draft Memo")

if st.button("Generate Summary"):
    st.markdown(memo_text)
