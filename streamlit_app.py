import streamlit as st
import pandas as pd

data = {
    "Category": [
        "Design Process Steps", "Design Process Steps", "Design Process Steps", "Design Process Steps", "Design Process Steps", "Design Process Steps",
        "Recurrence Interval", "Recurrence Interval", "Recurrence Interval", "Recurrence Interval", "Recurrence Interval",
        "Hydrologic Methods", "Hydrologic Methods", "Hydrologic Methods",
        "Stormwater Management", "Stormwater Management", "Stormwater Management", "Stormwater Management", "Stormwater Management",
        "Allowable Water Surface Elevation", "Allowable Water Surface Elevation", "Allowable Water Surface Elevation", "Allowable Water Surface Elevation", "Allowable Water Surface Elevation",
        "Drainage Permit Checklist", "Drainage Permit Checklist", "Drainage Permit Checklist", "Drainage Permit Checklist", "Drainage Permit Checklist", "Drainage Permit Checklist",
        "Time of Concentration", "Time of Concentration",
        "Channel Design", "Channel Design", "Channel Design",
        "Stormwater Storage", "Stormwater Storage", "Stormwater Storage", "Stormwater Storage", "Stormwater Storage",
        "Permits & Regulatory Agencies", "Permits & Regulatory Agencies", "Permits & Regulatory Agencies", "Permits & Regulatory Agencies", "Permits & Regulatory Agencies"
    ],
    "Item": [
        "Preliminary Investigation", "Site Analysis", "Choose Recurrence Interval", "Hydrologic Analysis", "Hydraulic Design", "Environmental Review",
        "Freeway/Interstate Cross Drain", "Service Highway Cross Drain", "Longitudinal Pipe – Freeway", "Longitudinal Pipe – Service Hwy", "NJDEP Permit Area",
        "< 20 acres", "< 5 sq mi", "> 1 acre",
        "Water Quantity", "Water Quality", "Recharge", "Nonstructural BMPs First", "Permit Required?",
        "Residence", "Culvert (new)", "Culvert (existing)", "Channel", "Storm Sewer Grate/Rim",
        "Existing Pipes Cleaned", "No Watershed Diversion", "Outfall Protection", "BMPs on Developer Property", "Drainage Calcs Submitted", "ROW and Inlets Shown",
        "Minimum Tc = 10 mins", "Flow Types (sheet, gutter, pipe, channel)",
        "Grassed Channel", "Non-erodible Channel", "Permitting Considerations",
        "Detention Basin", "Retention Basin", "Outlet Design (Weir/Orifice)", "Modeling Tools", "Design Tip",
        "NJDEP FHACA Permit", "Soil Erosion & Sediment Control", "NJPDES Permit", "Pinelands/Highlands/CAFRA", "Category 1 Waters (C1)"
    ],
    "Details": [
        "Gather maps, drainage, topo, permits", "Assess drainage area, stream, soils, permits", "Use Table 10-2 to select interval", "Use Rational, TR-55, or TR-20", "Storm drains, culverts, channels", "Assess TSS, recharge, quantity control",
        "50-year", "25-year", "15-year", "10-year", "100-year",
        "Use Rational Method", "Use TR-55", "Use TR-20, HEC-HMS",
        "If > 0.25 ac. impervious", "80% TSS Removal", "Infiltrate 2-yr storm volume increase", "Use unless not feasible", "If ≥ 1 acre disturbed",
        "Basement floor/window elevation", "Top of new culvert", "Outside road edge", "1 ft below top of bank", "1 ft below grate/rim",
        "System must be clear and functional", "Don’t redirect flow to another watershed", "Show stone size, width, length", "Onsite and with maintenance plan", "2-, 10-, 25-, 100-year storms shown", "Show all ROW, pipes, inlets",
        "Sum of travel times ≥ 10 min", "Sheet, gutter, pipe, open channel",
        "Preferred type where feasible", "Use in erosive or steep slopes", "Check floodplain or C1 permit needs",
        "Temporary storage, drains after storm", "Permanent pool of water", "Q=CA(2gH)^0.5 or Q=CLH^1.5", "Use HEC-1, TR-20, Pond-2", "Use multi-stage outlets if needed",
        "Needed if encroaching streams/floodplain", "≥ 5,000 sq ft disturbed (non-NJDOT only)", "≥ 1 acre disturbed", "Check project location", "300-ft buffer unless previously disturbed"
    ]
}

# Build DataFrame
df = pd.DataFrame(data)

# App UI
st.set_page_config(page_title="NJ Drainage Tool", page_icon="💧")
st.title("💧 NJ Drainage Design Lookup Tool")

# Dropdowns
category = st.selectbox("1. Choose a Category", sorted(df["Category"].unique()))
filtered = df[df["Category"] == category]
item = st.selectbox("2. Choose an Item", filtered["Item"])
detail = filtered[filtered["Item"] == item]["Details"].values[0]

# Output
st.markdown("### 3. Design Guidance:")
st.success(detail)

st.markdown("---")
st.caption("Based on NJDOT Roadway Design Manual – Section 10")
