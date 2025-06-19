import streamlit as st

# Verified NJDOT-based guidance per component
manuals = {
    "NJDOT Roadway Design Manual – Section 10": {
        "Inlet": {
            "Inlet Type": ["- Curb, grate, or combo inlet (based on drainage area and slope)"],
            "Manning's n (Inlet)": ["- Use 0.013 for paved surfaces (Table 10-6)"],
            "Longitudinal Slope (Inlet)": ["- ≥ 0.005 ft/ft (0.5%) for gutter flow"],
            "Road Cross Slope (ft/ft)": ["- 0.020 (2%) typical per roadway section"],
            "Rainfall Intensity (in/hr)": ["- Use Table 10-2 for location-based intensity"],
            "Max Spread (ft)": ["- ≤ 6.0 ft to avoid encroachment into travel lane"],
            "Catch Basin Spacing": ["- Start with 150 ft; refine based on spread and gutter slope"]
        },
        "Pipe": {
            "Conduit Type": ["- Use RCP, PVC, or HDPE per Table 10-4"],
            "Diameter / Size": ["- Minimum 15\" required for public ROW"],
            "Manning's n": ["- 0.012–0.015 based on material (Table 10-6)"],
            "Slope": ["- Minimum 0.005 ft/ft preferred", "- Maintain 2.5 fps flow velocity"]
        },
        "Manhole": {
            "Elevation (Invert) (ft)": ["- Invert must allow 0.1–0.3 ft drop through manhole"],
            "Structure Type": ["- Circular for pipes ≤ 24 in; rectangular if larger or multiple lines"],
            "Diameter (ft)": ["- ≥ 4.0 ft for maintenance access"],
            "Headloss Method": ["- Use HEC-22 Energy method as standard"]
        },
        "Catchment": {
            "Runoff Method": ["- Rational Method for drainage areas < 20 acres"],
            "Runoff Coefficient (Rational)": ["- Use Table 10-6 for C values (0.30–0.90)"],
            "Time of Concentration (min)": ["- Minimum Tc = 10 minutes (design requirement)"]
        },
        "Outfall": {
            "Boundary Condition Type": ["- Free Outfall unless stage/tailwater defined"],
            "Elevation (Invert) (ft)": ["- Match last pipe invert for continuous drainage"]
        }
    },

    "NJDOT Bridge & Structures Manual – Section 22": {
        "Inlet": {
            "Inlet Type": ["- Use catalog slot drains or bridge inlets per Section 22.9"],
            "Manning's n (Inlet)": ["- 0.012 for concrete bridge deck surfaces"],
            "Road Cross Slope (ft/ft)": ["- 2% slope typical for bridge decks"],
            "Rainfall Intensity (in/hr)": ["- Use 3.0 in/hr design storm for bridges"],
            "Catch Basin Spacing": ["- Begin with 100 ft spacing; adjust per spread analysis"]
        },
        "Pipe": {
            "Diameter / Size": ["- Size pipes for 10- to 15-year storm event under bridge"],
            "Manning's n": ["- 0.011–0.013 typical for RCP or VCP"],
            "Slope": ["- Minimum 0.005 ft/ft recommended"]
        },
        "Manhole": {
            "Structure Type": ["- Circular preferred for bridge deck structures"],
            "Headloss Method": ["- Use HEC-22 Energy method standard"]
        },
        "Catchment": {
            "Runoff Method": ["- Rational Method required for bridge drainage"],
            "Runoff Coefficient (Rational)": ["- Use C = 0.90 for bridge deck (impervious)"],
            "Time of Concentration (min)": ["- Minimum Tc = 10 min unless bridge deck is shorter"]
        },
        "Outfall": {
            "Boundary Condition Type": ["- Free outfall unless discharging into a known stage zone"],
            "Elevation (Invert) (ft)": ["- Align with last pipe for outlet control"]
        }
    }
}

# Streamlit App
st.set_page_config("NJDOT StormCAD Guide", page_icon="🛠️")
st.title("🧾 NJDOT StormCAD Input Field Reference")

# Manual and Component Selector
manual = st.selectbox("📘 Select Manual", manuals.keys())
component = st.radio("📂 Select Component", ["Inlet", "Pipe", "Manhole", "Catchment", "Outfall"])
fields = manuals[manual][component]

# Display Filtered Fields
st.subheader(f"🛠️ {component} Fields – Verified from {manual}")
for field, guidance in fields.items():
    st.text_area(field, "\n".join(guidance), height=100, disabled=True)

st.markdown("---")
st.caption("Only fields with verified NJDOT manual references are shown.")
