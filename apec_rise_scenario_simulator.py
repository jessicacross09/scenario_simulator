import streamlit as st
import pandas as pd

# Load enhanced scenario matrix
@st.cache_data
def load_data():
    return pd.read_csv("enhanced_apec_rise_scenario_matrix.csv")

df = load_data()

# Streamlit App UI
st.set_page_config(page_title="APEC-RISE Scenario Simulator", layout="centered")
st.title("🧭 APEC-RISE Scenario Planning Simulator")
st.caption("Explore adaptation strategies by assumption, scenario, region, and workstream. Based on PMP Table 15.")

# Filters
region = st.selectbox("🌍 Select Region", options=df["Region"].unique())
workstream = st.selectbox("🧩 Select Workstream", options=df["Workstream"].unique())

filtered_df = df[(df["Region"] == region) & (df["Workstream"] == workstream)]

assumption = st.selectbox("🔹 Select a critical assumption", filtered_df["Assumption"].unique())
scenario = st.radio("🔸 Select a scenario", ["Baseline", "Optimistic", "Pessimistic"])

# Scenario icons
scenario_icons = {
    "Baseline": "🟡",
    "Optimistic": "🟢",
    "Pessimistic": "🔴"
}

# Display result
row = filtered_df[(filtered_df["Assumption"] == assumption) & (filtered_df["Scenario"] == scenario)]

if not row.empty:
    st.subheader(f"{scenario_icons[scenario]} Scenario: {scenario}")
    
    st.markdown("### 🚨 Trigger")
    st.info(row["Trigger"].values[0])

    st.markdown("### 🛠️ Adaptation Strategy")
    st.success(row["Adaptation"].values[0])
else:
    st.warning("No data found for this combination.")

# Expandable summary table
with st.expander("📊 View all scenarios for this assumption"):
    summary = filtered_df[filtered_df["Assumption"] == assumption][["Scenario", "Trigger", "Adaptation"]]
    st.dataframe(summary, use_container_width=True)

# Download scenario summary
if not row.empty:
    download_text = f"""APEC-RISE Scenario Plan

Assumption: {assumption}
Region: {region}
Workstream: {workstream}
Scenario: {scenario}
Trigger: {row['Trigger'].values[0]}
Adaptation Strategy: {row['Adaptation'].values[0]}
"""
    st.download_button("📥 Download Scenario Summary", data=download_text, file_name="scenario_summary.txt")

# Footer
st.divider()
st.caption("U.S. APEC-RISE MEL Tool – Enhanced Scenario Simulator (PMP Table 15)")

