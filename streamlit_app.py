import streamlit as st

# Updated manuals with StormCAD-relevant design inputs
manuals = {
    "NJDOT Roadway Design Manual – Section 10": {
        "Pipe Design": "Use 10-year storm for service roads, 15-year for freeways. Rational method for < 20 ac, TR-55 for < 5 sq mi.",
        "Time of Concentration": "Minimum Tc = 10 minutes. Combine flow segments: sheet, shallow, pipe, and channel.",
        "Outlet Structure": "Use:\n- Q = CA(2gH)^0.5 for orifice\n- Q = CLH^1.5 for weir\nDesign for multi-stage release when needed.",
        "Quantity Control": "Must not exceed pre-development peak flow for 2-, 10-, 25-, and 100-year events.",
        "Culvert Sizing": "25-year storm for service roads, 50-year for interstate. Design for no overtopping at design flow."
    },
    "NJDOT Bridge & Structures Manual – Section 22": {
        "Bridge Deck Drainage (StormCAD Input)": (
            "- **Rational C**: Use 0.9 for impervious bridge deck\n"
            "- **Rainfall Intensity**: Use 3 in/hr for inlet spacing\n"
            "- **Max Spread at Curb**: ≤ 6 ft\n"
            "- **Cross Slope**: 2% (typical)\n"
            "- **Longitudinal Slope**: Prefer 0.5% min\n"
            "- **Inlet Type**: Curb opening inlets at low points\n"
            "- **Outlet Slope**: Follow pipe diameter guidelines\n"
        ),
        "Gutter Flow Analysis": (
            "Calculate gutter flow width using cross slope, longitudinal slope, and intensity.\n"
            "Use standard equations built into StormCAD or CivilStorm.\n"
            "Ensure spread ≤ 6 ft in all locations."
        ),
        "Catch Basin Placement": (
            "Place catch basins near bridge ends, sag points, and crown transitions.\n"
            "Spacing depends on flow, slope, and deck geometry — start with max 100 ft and refine with model."
        )
    }
}

# App config
st.set_page_config(page_title="Drainage Design Requirement Lookup", page_icon="🌧️")
st.title("🌧️ Drainage & Environmental Design Requirements Lookup")

# Description block
st.markdown("""
This tool provides task-based drainage and stormwater design guidance for NJDOT projects.  
It extracts key requirements from Section 10 (Roadway Design) and Section 22 (Bridge & Structures) relevant to drainage modeling, StormCAD setup, and permitting thresholds.
""")

# Dropdown 1 – Select Manual
selected_manual = st.selectbox("Select a Manual", list(manuals.keys()))

# Dropdown 2 – Select Design Topic
topics = list(manuals[selected_manual].keys())
selected_topic = st.selectbox("Select a Design Task or Topic", topics)

# Output
st.markdown("### Design Guidance:")
st.success(manuals[selected_manual][selected_topic])

st.markdown("---")
st.caption("Sources: NJDOT Design Manuals – Roadway Section 10 and Structures Section 22")

