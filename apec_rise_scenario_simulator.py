import streamlit as st
import pandas as pd

# Load the scenario matrix with flags
df = pd.read_csv("full_apec_rise_scenario_matrix.csv")

st.set_page_config(page_title="APEC-RISE Scenario Simulator", layout="centered")
st.title("🧭 APEC-RISE Scenario Planning Simulator")
st.caption("Explore risk triggers and adaptation strategies across 21 APEC economies.")

# Dropdowns for filters
economy = st.selectbox("🌐 Select Economy", sorted(df["Economy"].unique()))
workstream = st.selectbox("🧩 Select Workstream", sorted(df["Workstream"].unique()))
filtered_df = df[(df["Economy"] == economy) & (df["Workstream"] == workstream)]

assumption = st.selectbox("🔹 Select Assumption", filtered_df["Assumption"].unique())
scenario = st.radio("🔸 Select Scenario", ["Baseline", "Optimistic", "Pessimistic"])

# Icons for scenario and flag display
icons = {"Baseline": "🟡", "Optimistic": "🟢", "Pessimistic": "🔴"}
flag_icons = {
    "High Risk": "🔴",
    "High Priority": "⭐",
    "Sensitive": "🔒"
}

# Filter based on full selection
row = filtered_df[(filtered_df["Assumption"] == assumption) & (filtered_df["Scenario"] == scenario)]
if not row.empty:
    flag_str = str(row["Flags"].values[0])
    flag_display = " ".join([flag_icons.get(f.strip(), f.strip()) for f in flag_str.split(",") if f.strip()])
    st.subheader(f"{icons[scenario]} Scenario: {scenario}  {flag_display}")
    st.markdown("### 🚨 Trigger")
    st.info(str(row["Trigger"].values[0]))
    st.markdown("### 🛠️ Adaptation Strategy")
    st.success(str(row["Adaptation"].values[0]))

    # Summary for download
    summary_template = """APEC-RISE Scenario Plan

Economy: {economy}
Workstream: {workstream}
Assumption: {assumption}
Scenario: {scenario}
Trigger: {trigger}
Adaptation Strategy: {adaptation}
Flags: {flags}
"""
    summary = summary_template.format(
        economy=economy,
        workstream=workstream,
        assumption=assumption,
        scenario=scenario,
        trigger=row["Trigger"].values[0],
        adaptation=row["Adaptation"].values[0],
        flags=flag_str
    )
    st.download_button("📥 Download Scenario Summary", data=summary, file_name="scenario_summary.txt")
else:
    st.warning("No data found for this combination.")

# View all scenarios for the selected assumption
with st.expander("📊 View all scenarios for this assumption"):
    st.dataframe(
        filtered_df[filtered_df["Assumption"] == assumption][["Scenario", "Trigger", "Adaptation", "Flags"]],
        use_container_width=True
    )

st.divider()
st.caption("U.S. APEC-RISE M&E Scenario Simulator")
