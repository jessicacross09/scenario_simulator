import streamlit as st
import pandas as pd

# Define sample scenario matrix from PMP Table 15
data = [
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
    }
]

# Convert data into a DataFrame
df = pd.DataFrame(data)

# App UI
st.set_page_config(page_title="APEC-RISE Scenario Simulator", layout="centered")
st.title("🧭 APEC-RISE Scenario Planning Simulator")
st.caption("Use this tool to explore risk scenarios and program adaptation strategies based on PMP Table 15.")

# Select filters
assumption = st.selectbox("🔹 Select a critical assumption", df["Assumption"].unique())
scenario = st.radio("🔸 Select a scenario", ["Baseline", "Optimistic", "Pessimistic"])

# Filter DataFrame
row = df[(df["Assumption"] == assumption) & (df["Scenario"] == scenario)]

# Display results
if not row.empty:
    st.markdown("### 🚨 Trigger")
    st.info(row["Trigger"].values[0])

    st.markdown("### 🛠️ Adaptation Strategy")
    st.success(row["Adaptation"].values[0])
else:
    st.warning("No data found for this combination.")

# Footer
st.divider()
st.caption("Based on the U.S. APEC-RISE Performance Management Plan (PMP) – Table 15.")
