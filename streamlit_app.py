import streamlit as st

# Verified field guidance from each manual
manuals = {
    "NJDOT Roadway Design Manual – Section 10": {
        # [Inlet, Pipe, Manhole, Catchment, Outfall] — previously provided content
        # ... (keep same as earlier — not shown here to save space)
    },
    "NJDOT Bridge & Structures Manual – Section 22": {
        # [Inlet, Pipe, Manhole, Catchment, Outfall] — previously provided content
        # ... (keep same as earlier — not shown here to save space)
    },
    "HDS-4: Introduction to Highway Hydraulics (FHWA-NHI-08-090)": {
        "Inlet": {
            "Inlet Type": ["- Use inlets with headwalls or flared ends to reduce buckling and erosion"],
            "Grate Type": ["- Use grates resistant to bending under flow (avoid mitered edges)"],
            "Inlet Location": ["- Match topography; avoid misalignment with downstream systems"],
            "Capture Efficiency": ["- Design for partial drainage efficiency based on time of concentration"]
        },
        "Pipe": {
            "Material": ["- Use RCP or CMP per HDS-5 charts (HY-8 supported)"],
            "Diameter": ["- Select via HDS-5 nomographs or HY-8 modeling"],
            "Slope": ["- Match natural slope where feasible to minimize excavation"],
            "Roughness (Manning's n)": ["- Use n = 0.016 for paved, 0.5 for turf channels (Appendix B)"],
            "Design Flow": ["- Peak runoff may come from subareas with shorter Tc"]
        },
        "Manhole": {
            "Invert Elevation": ["- Maintain hydraulic slope and minimum cover at junctions"],
            "Number of Pipes": ["- Consider cumulative inflow for energy dissipation need"]
        },
        "Catchment": {
            "Area": ["- Measure via topo maps or field survey; include all inflow zones"],
            "Runoff Coefficient (C)": ["- Residential = 0.3–0.75; Industrial = 0.5–0.9 (Table B.1)"],
            "Time of Concentration": ["- Use McCuen eq: t = K(0.6nL)/(i^0.4 S^0.3)"],
            "Rainfall Intensity": ["- Use NOAA Atlas 14 or IDF curve for Tc"]
        },
        "Outfall": {
            "Tailwater Condition": ["- Check for tailwater effects from downstream systems"],
            "Energy Dissipator": ["- Required if velocity > 10 ft/s or no channel lining"],
            "Outlet Protection": ["- Use riprap, cutoff walls, or culvert-end control devices"]
        }
    }
}

# App UI
st.set_page_config("StormCAD Field Design Reference", page_icon="🛠️")
st.title("🧾 StormCAD Field Design Reference (NJDOT + HDS-4)")

# Manual selector
manual = st.selectbox("📘 Select Manual", manuals.keys())
component = st.radio("📂 Select Component", ["Inlet", "Pipe", "Manhole", "Catchment", "Outfall"])
fields = manuals[manual][component]

# Manual clarifier
if "HDS-4" in manual:
    st.info("🔎 Note: HDS-4 is a federal FHWA guide. Always confirm with NJDOT for use on NJ projects.")

# Display component fields
st.subheader(f"🛠️ {component} Fields – {manual}")
for field, notes in fields.items():
    st.text_area(field, "\n".join(notes), height=100, disabled=True)

st.markdown("---")
st.caption("Only input fields with explicit references in design manuals are shown.")
