import streamlit as st

# Define design requirements by task/component
design_tasks = {
    "Pipe": "Design for:\n- 15-year storm (Freeway)\n- 10-year storm (Service Highway)\nUse Rational Method for < 20 acres or TR-55 for < 5 sq mi.",
    "Culvert – Interstate": "Design for 50-year storm (Table 10-2).\nConsider allowable water surface elevation at road edge.",
    "Culvert – Service Highway": "Design for 25-year storm.\nCheck for NJDEP permit area → use 100-year storm.",
    "Storm Sewer Inlet": "Water must be 1 ft below grate or rim elevation under design storm.",
    "Recharge Basin": "Must infiltrate increase in 2-year, 24-hour storm volume.\nUse site-specific soil data.",
    "Outlet Structure": "Use:\n- Q = CA(2gH)^0.5 for orifice\n- Q = CLH^1.5 for weir\nDesign for multi-stage release when needed.",
    "Channel – Grassed": "Preferred type where feasible.\nCheck slope, soil erodibility.",
    "Channel – Non-erodible": "Use on steep grades or where erosion is likely.\nLine with riprap, concrete, or gabion.",
    "Storage Basin (Detention)": "Design to prevent increase in peak flow for 2-, 10-, 25-, and 100-year storms.",
    "TSS Removal": "Design BMPs to remove 80% Total Suspended Solids.\nUse bioretention, filters, or wet ponds.",
    "Time of Concentration": "Minimum Tc = 10 minutes.\nUse travel time components: sheet flow, shallow flow, channel, pipe.",
    "Permitting Thresholds": "≥ 1 acre disturbed → NJDEP stormwater permit.\n≥ 5,000 sq ft disturbed (non-NJDOT) → Soil Erosion permit.\nFloodplain or water encroachment → NJDEP FHACA permit."
}

# Streamlit app UI
st.set_page_config(page_title="NJDOT Drainage Design Rules", page_icon="📐")
st.title("📐 NJDOT Drainage Design Assistant")

task = st.selectbox("What are you designing?", list(design_tasks.keys()))
st.markdown("### Design Requirements:")
st.success(design_tasks[task])

st.markdown("---")
st.caption("Based on NJDOT Design Manual – Section 10")

