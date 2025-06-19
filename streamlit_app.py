import streamlit as st

# Verified manual design guidance by element
manuals = {
    "NJDOT Roadway Design Manual – Section 10": {
        "Catch Basin": {
            "Inlet Type": ["- Curb, grate, or combo inlet (based on drainage area and slope)"],
            "Manning's n (Inlet)": ["- Use 0.013 for paved surfaces (Table 10-6)"],
            "Longitudinal Slope (Inlet)": ["- ≥ 0.005 ft/ft (0.5%) for gutter flow"],
            "Road Cross Slope (ft/ft)": ["- 0.020 (2%) typical per roadway section"],
            "Rainfall Intensity (in/hr)": ["- Use Table 10-2 for location-based intensity"],
            "Max Spread (ft)": ["- ≤ 6.0 ft to avoid encroachment into travel lane"],
            "Catch Basin Spacing": ["- Start with 150 ft; refine based on spread and gutter slope"]
        },
        "Pipe Properties": {
            "Conduit Type": ["- Use RCP, PVC, or HDPE per Table 10-4"],
            "Diameter / Size": ["- Minimum 15\" required for public ROW"],
            "Manning's n": ["- 0.012–0.015 based on material (Table 10-6)"],
            "Slope": ["- Minimum 0.005 ft/ft preferred", "- Maintain 2.5 fps flow velocity"]
        },
        "Manhole Properties": {
            "Elevation (Invert) (ft)": ["- Invert must allow 0.1–0.3 ft drop through manhole"],
            "Structure Type": ["- Circular for pipes ≤ 24 in; rectangular if larger or multiple lines"],
            "Diameter (ft)": ["- ≥ 4.0 ft for maintenance access"],
            "Headloss Method": ["- Use HEC-22 Energy method as standard"]
        },
        "Drainage Area Properties": {
            "Runoff Method": ["- Rational Method for drainage areas < 20 acres"],
            "Runoff Coefficient (Rational)": ["- Use Table 10-6 for C values (0.30–0.90)"],
            "Time of Concentration (min)": ["- Minimum Tc = 10 minutes (design requirement)"]
        },
        "Outfall Properties": {
            "Boundary Condition Type": ["- Free Outfall unless stage/tailwater defined"],
            "Elevation (Invert) (ft)": ["- Match last pipe invert for continuous drainage"]
        }
    },

    "NJDOT Bridge & Structures Manual – Section 22": {
        "Catch Basin": {
            "Inlet Type": ["- Use catalog slot drains or bridge inlets per Section 22.9"],
            "Manning's n (Inlet)": ["- 0.012 for concrete bridge deck surfaces"],
            "Road Cross Slope (ft/ft)": ["- 2% slope typical for bridge decks"],
            "Rainfall Intensity (in/hr)": ["- Use 3.0 in/hr design storm for bridges"],
            "Catch Basin Spacing": ["- Begin with 100 ft spacing; adjust per spread analysis"]
        },
        "Pipe Properties": {
            "Diameter / Size": ["- Size pipes for 10- to 15-year storm event under bridge"],
            "Manning's n": ["- 0.011–0.013 typical for RCP or VCP"],
            "Slope": ["- Minimum 0.005 ft/ft recommended"]
        },
        "Manhole Properties": {
            "Structure Type": ["- Circular preferred for bridge deck structures"],
            "Headloss Method": ["- Use HEC-22 Energy method standard"]
        },
        "Drainage Area Properties": {
            "Runoff Method": ["- Rational Method required for bridge drainage"],
            "Runoff Coefficient (Rational)": ["- Use C = 0.90 for bridge deck (impervious)"],
            "Time of Concentration (min)": ["- Minimum Tc = 10 min unless bridge deck is shorter"]
        },
        "Outfall Properties": {
            "Boundary Condition Type": ["- Free outfall unless discharging into a known stage zone"],
            "Elevation (Invert) (ft)": ["- Align with last pipe for outlet control"]
        }
    },

    "HDS-4: Introduction to Highway Hydraulics (FHWA-NHI-08-090)": {
        "Catch Basin": {
            "Inlet Type": ["- Use inlets with headwalls or flared ends to reduce buckling and erosion"],
            "Grate Type": ["- Use grates resistant to bending under flow (avoid mitered edges)"],
            "Inlet Location": ["- Match topography; avoid misalignment with downstream systems"],
            "Capture Efficiency": ["- Design for partial drainage efficiency based on time of concentration"]
        },
        "Pipe Properties": {
            "Material": ["- Use RCP or CMP per HDS-5 charts (HY-8 supported)"],
            "Diameter": ["- Select via HDS-5 nomographs or HY-8 modeling"],
            "Slope": ["- Match natural slope where feasible to minimize excavation"],
            "Roughness (Manning's n)": ["- Use n = 0.016 for paved, 0.5 for turf channels (Appendix B)"],
            "Design Flow": ["- Peak runoff may come from subareas with shorter Tc"]
        },
        "Manhole Properties": {
            "Invert Elevation": ["- Maintain hydraulic slope and minimum cover at junctions"],
            "Number of Pipes": ["- Consider cumulative inflow for energy dissipation need"]
        },
        "Drainage Area Properties": {
            "Area": ["- Measure via topo maps or field survey; include all inflow zones"],
            "Runoff Coefficient (C)": ["- Residential = 0.3–0.75; Industrial = 0.5–0.9 (Table B.1)"],
            "Time of Concentration": ["- Use McCuen eq: t = K(0.6nL)/(i^0.4 S^0.3)"],
            "Rainfall Intensity": ["- Use NOAA Atlas 14 or IDF curve for Tc"]
        },
        "Outfall Properties": {
            "Tailwater Condition": ["- Check for tailwater effects from downstream systems"],
            "Energy Dissipator": ["- Required if velocity > 10 ft/s or no channel lining"],
            "Outlet Protection": ["- Use riprap, cutoff walls, or culvert-end control devices"]
        }
    }
}

# Streamlit Setup
st.set_page_config("StormCAD Manual Regulations", page_icon="🛠️")
st.title("🧾 StormCAD Manual Regulations")

# Manual & Element Selection
manual = st.selectbox("📘 Select Manual", manuals.keys())
element = st.radio("📂 Select Element Symbology", list(manuals[manual].keys()))
fields = manuals[manual][element]

# Clarifier for HDS-4
if "HDS-4" in manual:
    st.info("🔎 Note: HDS-4 is a federal FHWA guide. Always confirm with NJDOT for use on NJ projects.")

# Field display
st.subheader(f"🛠️ {element} – {manual}")
for field, guidance in fields.items():
    st.text_area(field, "\n".join(guidance), height=100, disabled=True)

st.markdown("---")
st.caption("Only StormCAD input fields with verified references in NJDOT or FHWA manuals are included.")
