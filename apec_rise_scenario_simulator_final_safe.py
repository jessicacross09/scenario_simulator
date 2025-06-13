import streamlit as st
import pandas as pd

# Embedded data with string-formatted flags
data = [
    # (shortened for readability – insert full 1,260-row data dict here in practice)
    # Sample row:
    {
        "Economy": "Vietnam",
        "Workstream": "Trade Policy",
        "Assumption": "Stakeholder alignment with U.S. priorities",
        "Scenario": "Pessimistic",
        "Trigger": "Difficulties gaining stakeholder buy-in or moving U.S. priorities forward",
        "Adaptation": "Intensify diplomatic engagement; tailor technical assistance; focus on institutional champions; document resistance for follow-up",
        "Flags": "High Risk, Sensitive"
    },
    # ... add all other rows here ...
]

df = pd.DataFrame(data)

st.set_page_config(page_title="APEC-RISE Full Scenario Simulator", layout="centered")
st.title("🧭 APEC-RISE Scenario Planning Simulator")
st.caption("Select an economy, workstream, assumption, and scenario to explore triggers, responses, and strategic flags.")

economy = st.selectbox("🌐 Select Economy", sorted(df["Economy"].unique()))
workstream = st.selectbox("🧩 Select Workstream", sorted(df["Workstream"].unique()))
filtered_df = df[(df["Economy"] == economy) & (df["Workstream"] == workstream)]

assumption = st.selectbox("🔹 Select Assumption", filtered_df["Assumption"].unique())
scenario = st.radio("🔸 Select Scenario", ["Baseline", "Optimistic", "Pessimistic"])

icons = {"Baseline": "🟡", "Optimistic": "🟢", "Pessimistic": "🔴"}
flag_icons = {
    "High Risk": "🔴",
    "High Priority": "⭐",
    "Sensitive": "🔒"
}

row = filtered_df[(filtered_df["Assumption"] == assumption) & (filtered_df["Scenario"] == scenario)]
if not row.empty:
    flag_str = str(row["Flags"].values[0])
    flag_display = " ".join([flag_icons.get(f.strip(), f.strip()) for f in flag_str.split(",") if f.strip()])
    st.subheader(f"{icons[scenario]} Scenario: {scenario}  {flag_display}")
    st.markdown("### 🚨 Trigger")
    st.info(str(row["Trigger"].values[0]))
    st.markdown("### 🛠️ Adaptation Strategy")
    st.success(str(row["Adaptation"].values[0]))

    # Generate summary text using safe .format()
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
        trigger=row['Trigger'].values[0],
        adaptation=row['Adaptation'].values[0],
        flags=flag_str
    )

    st.download_button("📥 Download Scenario Summary", data=summary, file_name="scenario_summary.txt")

else:
    st.warning("No data found for this combination.")

with st.expander("📊 View all scenarios for this assumption"):
    st.dataframe(
        filtered_df[filtered_df["Assumption"] == assumption][["Scenario", "Trigger", "Adaptation", "Flags"]],
        use_container_width=True
    )

st.divider()
st.caption("U.S. APEC-RISE M&E Scenario Planning Simulator")
