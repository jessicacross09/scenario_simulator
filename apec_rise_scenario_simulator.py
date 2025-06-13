import streamlit as st
import pandas as pd

# Embedded scenario matrix data (Economy instead of Region)
data = [
    {"Assumption": "Stakeholder alignment with U.S. priorities", "Scenario": "Baseline", "Trigger": "Responsiveness of APEC stakeholders to U.S. priorities", "Adaptation": "Proceed with technical dialogues and co-creation efforts as planned", "Workstream": "Trade Policy", "Economy": "Viet Nam"},
    {"Assumption": "Stakeholder alignment with U.S. priorities", "Scenario": "Optimistic", "Trigger": "High alignment with U.S. goals", "Adaptation": "Expand collaboration with aligned economies; increase visibility of U.S.-led initiatives", "Workstream": "Trade Policy", "Economy": "Vietnam"},
    {"Assumption": "Stakeholder alignment with U.S. priorities", "Scenario": "Pessimistic", "Trigger": "Difficulties gaining stakeholder buy-in or moving U.S. priorities forward", "Adaptation": "Intensify diplomatic engagement; tailor technical assistance; focus on institutional champions; document resistance for follow-up", "Workstream": "Trade Policy", "Economy": "Vietnam"},

    {"Assumption": "Political and institutional continuity", "Scenario": "Baseline", "Trigger": "Stable environment", "Adaptation": "Maintain current schedule and engagement levels", "Workstream": "Economic Governance", "Economy": "Papua New Guinea"},
    {"Assumption": "Political and institutional continuity", "Scenario": "Optimistic", "Trigger": "Increased institutional cooperation", "Adaptation": "Strengthen long-term partnerships and deepen policy coordination", "Workstream": "Economic Governance", "Economy": "Papua New Guinea"},
    {"Assumption": "Political and institutional continuity", "Scenario": "Pessimistic", "Trigger": "Instability or disrupted coordination", "Adaptation": "Shift resources to stable economies; support resilience and contingency planning", "Workstream": "Economic Governance", "Economy": "Papua New Guinea"},

    {"Assumption": "Policy and regulatory openness", "Scenario": "Baseline", "Trigger": "Expected receptivity", "Adaptation": "Maintain steady reform support and technical assistance", "Workstream": "Regulatory Reform", "Economy": "China"},
    {"Assumption": "Policy and regulatory openness", "Scenario": "Optimistic", "Trigger": "High receptivity to U.S. policy recommendations", "Adaptation": "Accelerate pilot reforms and highlight results", "Workstream": "Regulatory Reform", "Economy": "China"},
    {"Assumption": "Policy and regulatory openness", "Scenario": "Pessimistic", "Trigger": "Declining openness or regulatory pushback", "Adaptation": "Refocus engagement; seek alternate entry points or incremental reforms; monitor policy resistance", "Workstream": "Regulatory Reform", "Economy": "China"},

    {"Assumption": "Digital and infrastructure readiness", "Scenario": "Baseline", "Trigger": "Sufficient readiness", "Adaptation": "Proceed with digital activities as planned", "Workstream": "Digital Economy", "Economy": "Philippines"},
    {"Assumption": "Digital and infrastructure readiness", "Scenario": "Optimistic", "Trigger": "Expanded digital readiness", "Adaptation": "Scale virtual engagements; introduce more advanced tools", "Workstream": "Digital Economy", "Economy": "Philippines"},
    {"Assumption": "Digital and infrastructure readiness", "Scenario": "Pessimistic", "Trigger": "Limited access or resistance to digital platforms", "Adaptation": "Use hybrid or offline delivery; increase support and training", "Workstream": "Digital Economy", "Economy": "Philippines"},

    {"Assumption": "Responsible local ownership", "Scenario": "Baseline", "Trigger": "Cost-sharing and local uptake sustained", "Adaptation": "Continue monitoring and co-planning", "Workstream": "Capacity Building", "Economy": "Indonesia"},
    {"Assumption": "Responsible local ownership", "Scenario": "Optimistic", "Trigger": "High commitment and ownership", "Adaptation": "Increase handover planning", "Workstream": "Capacity Building", "Economy": "Indonesia"},
    {"Assumption": "Responsible local ownership", "Scenario": "Pessimistic", "Trigger": "Low contribution or interest in uptake", "Adaptation": "Document gaps; adapt support model; focus on institutional champions", "Workstream": "Capacity Building", "Economy": "Indonesia"}
]

df = pd.DataFrame(data)

# Streamlit App UI
st.set_page_config(page_title="APEC-RISE Scenario Simulator", layout="centered")
st.title("🧭 APEC-RISE Scenario Planning Simulator")
st.caption("Explore adaptation strategies by assumption, scenario, economy, and workstream. Based on PMP Table 15.")

# Filters
economy = st.selectbox("🌐 Select Economy", options=df["Economy"].unique())
workstream = st.selectbox("🧩 Select Workstream", options=df["Workstream"].unique())
filtered_df = df[(df["Economy"] == economy) & (df["Workstream"] == workstream)]

assumption = st.selectbox("🔹 Select a critical assumption", filtered_df["Assumption"].unique())
scenario = st.radio("🔸 Select a scenario", ["Baseline", "Optimistic", "Pessimistic"])

# Scenario icons
scenario_icons = {
    "Baseline": "🟡",
    "Optimistic": "🟢",
    "Pessimistic": "🔴"
}

# Display selected scenario
row = filtered_df[(filtered_df["Assumption"] == assumption) & (filtered_df["Scenario"] == scenario)]
if not row.empty:
    st.subheader(f"{scenario_icons[scenario]} Scenario: {scenario}")
    st.markdown("### 🚨 Trigger")
    st.info(row["Trigger"].values[0])
    st.markdown("### 🛠️ Adaptation Strategy")
    st.success(row["Adaptation"].values[0])
else:
    st.warning("No data found for this combination.")

# Scenario summary table
with st.expander("📊 View all scenarios for this assumption"):
    summary = filtered_df[filtered_df["Assumption"] == assumption][["Scenario", "Trigger", "Adaptation"]]
    st.dataframe(summary, use_container_width=True)

# Optional download
if not row.empty:
    download_text = f"""APEC-RISE Scenario Plan

Assumption: {assumption}
Economy: {economy}
Workstream: {workstream}
Scenario: {scenario}
Trigger: {row['Trigger'].values[0]}
Adaptation Strategy: {row['Adaptation'].values[0]}
"""
    st.download_button("📥 Download Scenario Summary", data=download_text, file_name="scenario_summary.txt")

# Footer
st.divider()
st.caption("U.S. APEC-RISE M^E Tool Scenario Planning Simulator)")
