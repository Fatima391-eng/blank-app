import streamlit as st
import pandas as pd

# Full set of sample data for NJDOT drainage design
data = {
    "Category": [
        "Design Process Steps", "Design Process Steps", "Design Process Steps",
        "Recurrence Interval", "Recurrence Interval",
        "Hydrologic Methods", "Hydrologic Methods",
        "Stormwater Management", "Stormwater Management", "Stormwater Management",
        "Permits & Agencies", "Permits & Agencies"
    ],
    "Item": [
        "Preliminary Investigation", "Site Analysis", "Hydrologic Analysis",
        "Freeway/Interstate Cross Drain", "Service Highway Cross Drain",
        "Rational Method", "TR-55",
        "Water Quantity", "Water Quality", "Recharge",
        "NJDEP FHACA Permit", "Soil Erosion & Sediment Control"
    ],
    "Details": [
        "Gather maps, drainage, topo, permits",
        "Assess drainage area, stream, soils, permits",
        "Use Rational, TR-55, or TR-20 depending on watershed",
        "50-year recurrence interval required",
        "25-year recurrence interval required",
        "Use for < 20 acres drainage areas",
        "Use for < 5 sq mi watershed areas",
        "Prevent increase in peak discharge and volume",
        "Must reduce Total Suspended Solids by 80%",
        "Infiltrate volume increase from 2-year storm",
        "Required for floodplain or regulated water encroachments",
        "Required for disturbing > 5,000 sq ft (non-NJDOT projects)"
    ]
}

df = pd.DataFrame(data)

st.set_page_config(page_title="NJ Drainage Tool", page_icon="💧")
st.title("💧 NJ Drainage Design Lookup Tool")

category = st.selectbox("1. Choose a Category", sorted(df["Category"].unique()))
filtered = df[df["Category"] == category]
item = st.selectbox("2. Choose an Item", filtered["Item"])
detail = filtered[filtered["Item"] == item]["Details"].values[0]

st.markdown("### 3. Design Guidance:")
st.success(detail)

st.markdown("---")
st.caption("Based on NJDOT Roadway Design Manual – Section 10")
