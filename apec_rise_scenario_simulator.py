import streamlit as st
import pandas as pd

# Full scenario matrix from PMP Table 15
data = [
    # Stakeholder alignment
    {
        "Assumption": "Stakeholder alignment with U.S. priorities",
        "Scenario": "Baseline",
        "Trigger": "Responsiveness of APEC stakeholders to U.S. priorities",
        "Adaptation": "Proceed with technical dialogues and co-creation efforts as planned"
    },
    {
        "Assumption": "Stakeholder alignment with U.S. priorities",
        "Scenario": "Optimistic",
        "Trigger": "High alignment with U.S. goals",
        "Adaptation": "Expand collaboration with aligned economies; increase visibility of U.S.-led initiatives"
    },
    {
        "Assumption": "Stakeholder alignment with U.S. priorities",
        "Scenario": "Pessimistic",
        "Trigger": "Difficulties gaining stakeholder buy-in or moving U.S. priorities forward",
        "Adaptation": "Intensify diplomatic engagement; tailor technical assistance; focus on institutional champions; document resistance for follow-up"
    },
    # Political and institutional continuity
    {
        "Assumption": "Political and institutional continuity",
        "Scenario": "Baseline",
        "Trigger": "Stable environment",
        "Adaptation": "Maintain current schedule and engagement levels"
    },
    {
        "Assumption": "Political and institutional continuity",
        "Scenario": "Optimistic",
        "Trigger": "Increased institutional cooperation",
        "Adaptation": "Strengthen long-term partnerships and deepen policy coordination"
    },
    {
        "Assumption": "Political and institutional continuity",
        "Scenario": "Pessimistic",
        "Trigger": "Instability or disrupted coordination",
        "Adaptation": "Shift resources to stable economies; support resilience and contingency planning"
    },
    # Policy and regulatory openness
    {
        "Assumption": "Policy and regulatory openness",
        "Scenario": "Baseline",
        "Trigger": "Expected receptivity",
        "Adaptation": "Maintain steady reform support and technical assistance"
    },
    {
        "Assumption": "Policy and regulatory openness",
        "Scenario": "Optimistic",
        "Trigger": "High receptivity to U.S. policy recommendations",
        "Adaptation": "Accelerate pilot reforms and highlight results"
    },
    {
        "Assumption": "Policy and regulatory openness",
        "Scenario": "Pessimistic",
        "Trigger": "Declining openness or regulatory pushback",
        "Adaptation": "Refocus engagement; seek alternate entry points or incremental reforms; monitor policy resistance"
    },
    # Digital and infrastructure readiness
    {
        "Assumption": "Digital and infrastructure readiness",
        "Scenario": "Baseline",
        "Trigger": "Sufficient readiness",
        "Adaptation": "Proceed with digital activities as planned"
    },
    {
        "Assumption": "Digital and infrastructure readiness",
        "Scenario": "Optimistic",
        "Trigger": "Expanded digital readiness",
        "Adaptation": "Scale virtual engagements; introduce more advanced tools"
    },
    {
        "Assumption": "Digital and infrastructure readiness",
        "Scenario": "Pessimistic",
        "Trigger": "Limited access or resistance to digital platforms",
        "Adaptation": "Use hybrid or offline delivery; increase support and training"
    },
    # Responsible local ownership
    {
        "Assumption": "Responsible local ownership",
        "Scenario": "Baseline",
        "Trigger": "Cost-sharing and local uptake sustained",
        "Adaptation": "Continue monitoring and co-planning"
    },
    {
        "Assumption": "Responsible local ownership",
        "Scenario": "Optimistic",
        "Trigger": "High commitment and ownership",
        "Adaptation": "Increase handover planning"
    },
    {
        "Assumption": "Responsible local ownership",
        "Scenario": "Pessimistic",
        "Trigger": "Low contribution or interest in uptake",
        "Adaptation": "Document gaps; adapt support model; focus on institutional champions"
    }
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Streamlit App UI
st.set_page_config(page_title="APEC-RISE Scenario Simulator", layout="centered")
st.title("🧭 APEC-RISE Scenario Planning Simulator")
st.caption("Explore program adaptation strategies if risk assumptions shift. Based on PMP Table 15.")

# User inputs
assumption = st.selectbox("🔹 Select a critical assumption", df["Assumption"].unique())
scenario = st.radio("🔸 Select a scenario", ["Baseline", "Optimistic", "Pessimistic"])

# Display results
row = df[(df["Assumption"] == assumption) & (df["Scenario"] == scenario)]

if not row.empty:
    st.markdown("### 🚨 Trigger")
    st.info(row["Trigger"].values[0])

    st.markdown("### 🛠️ Adaptation Strategy")
    st.success(row["Adaptation"].values[0])
else:
    st.warning("No data found for this combination.")

# Footer
st.divider()
st.caption("U.S. APEC-RISE M&E Tool – Scenario Planning Based on Performance Management Plan")

