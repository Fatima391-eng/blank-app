import streamlit as st

# Manual sources
manuals = {
    "NJDOT Roadway Design Manual – Section 10": {
        "Pipe": "Design for: 15-year storm (Freeway), 10-year storm (Service Hwy). Use Rational Method < 20 acres or TR-55 < 5 sq mi.",
        "Culvert – Interstate": "Design for 50-year storm. Check allowable water surface elevation.",
        "Recharge Basin": "Infiltrate volume from 2-year, 24-hour storm. Design with soil data.",
        "Outlet Structure": "Use Q = CA(2gH)^0.5 for orifice or Q = CLH^1.5 for weir. Design multi-stage where needed.",
        "Time of Concentration": "Minimum Tc = 10 minutes. Include sheet, shallow, pipe, and channel flow types.",
        "Permitting Thresholds": ">= 1 acre disturbed → NJDEP permit. >= 5000 sq ft → Soil Erosion. Encroachments → FHACA or others."
    },
    "NJDOT Bridge & Structures Manual (2016)": {
        "Deck Drainage": "Refer to Section 22. Provide inlets/downspouts to handle flow. Check cross slope and bridge end catch basins.",
        "Culverts": "See Section 29. Follow hydraulic criteria for waterway sizing. Use precast or cast-in-place box sections.",
        "Scour Protection": "Section 39. Required for piers and abutments in stream zones. Use riprap, cutoff walls, etc.",
        "Environmental Permits": "Section 42. Know when NJDEP, USACE, or Pinelands permits apply. Includes Stream Encroachment, Wetlands, CAFRA, etc.",
        "Integral Abutment Bridges": "Section 15. Hydraulics must be addressed if located near streams. Ensure no obstruction of flow or floodplain."
    }
}

# App config
st.set_page_config(page_title="Drainage Design Requirement Lookup", page_icon="🌧️")
st.title("🌧️ Drainage & Environmental Design Requirements Lookup")

# Dropdown 1 – Select Manual
selected_manual = st.selectbox("Select a Manual", list(manuals.keys()))

# Dropdown 2 – Select Design Topic
topics = list(manuals[selected_manual].keys())
selected_topic = st.selectbox("Select a Design Task or Topic", topics)

# Output
st.markdown("### Design Guidance:")
st.success(manuals[selected_manual][selected_topic])

st.markdown("---")
st.caption("Sources: NJDOT Design Manuals (Roadway & Structures)")

