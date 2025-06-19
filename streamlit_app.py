import streamlit as st

# Design rules mapped to specific components/tasks
design_tasks = {
    "Pipe": "Design for:\n- 15-year storm (Freeway)\n- 10-year storm (Service Highway)\nUse Rational Method for < 20 acres or TR-55 for < 5 sq mi.",
    "Culvert – Interstate": "Design for 50-year storm (Table 10-2).\nAllowable water surface should not exceed road shoulder.",
    "Culvert – Service Highway": "Design for 25-year storm.\nIf subject to NJDEP permitting, use 100-year storm instead.",
    "Storm Sewer Inlet": "Design so that water remains 1 ft below grate or rim elevation during design storm.",
    "Recharge Basin": "Must infiltrate the increase in runoff from the 2-year, 24-hour storm.\nUse site-specific infiltration rate and soil testing.",
    "Outlet Structure": "Use:\n- Q = CA(2gH)^0.5 for orifice\n- Q = CLH^1.5 for weir\nDesign multi-stage outlets if required for different storm events.",
    "Channel – Grassed": "Use where feasible to promote infiltration and reduce runoff velocity.\nEnsure slopes and soils are non-erodible under design flow.",
    "Channel – Non-erodible": "Required where slopes are steep or high-velocity flows exist.\nUse riprap, gabions, or concrete lining as appropriate.",
    "Storage Basin (Detention)": "Design to prevent increase in peak flows for 2-, 10-, 25-, and 100-year storms.\nVerify safe overflow and drawdown per NJDEP BMP Manual.",
    "TSS Removal": "Stormwater management systems must remove 80% Total Suspended Solids (TSS).\nBioretention, sand filters, and wet ponds are acceptable.",
    "Time of Concentration": "Minimum allowable Tc is 10 minutes.\nInclude components: sheet flow, shallow concentrated flow, channel/pipe flow.",
    "Permitting Thresholds": "≥ 1 acre disturbed → NJDEP stormwater permit required.\n≥ 5,000 sq ft disturbed (non-NJDOT) → Soil Erosion permit via SCD.\nFloodplain or regulated water → NJDEP FHACA permit."
}

# App layout
st.set_page_config(page_title="NJDOT Drainage Design Assistant", page_icon="📐")
st.title("📐 NJDOT Drainage Design Assistant")

# Intro description
st.markdown("""
This tool is a condensed, task-focused reference based on the **NJDOT Roadway Design Manual – Section 10: Drainage Design**.  
It summarizes essential design requirements — like storm frequencies, allowable elevations, outlet formulas, and permit triggers — organized by component, not by process.  
Rather than walking through procedure, it helps engineers quickly check what standard they need to design to for a specific drainage element.  
Ideal for real-world project workflows, it streamlines design decisions while ensuring NJDOT compliance.
""")

# User input
task = st.selectbox("What drainage element are you designing?", list(design_tasks.keys()))

# Output
st.markdown("### Design Requirements:")
st.success(design_tasks[task])

st.markdown("---")
st.caption("Based on NJDOT Roadway Design Manual – Section 10")
