import streamlit as st

# Complete NJDOT-based design guidance
manuals = {
    "NJDOT Roadway Design Manual – Section 10": {
        "Inlet": {
            "Inlet Type": ["- Curb, grate, or combo inlet", "- Match to runoff flow type"],
            "Inlet Location": ["- On grade or sag", "- Locate to intercept gutter flow"],
            "Manning's n (Inlet)": ["- Use 0.013 for pavement", "- Check Table 10-6 for other surfaces"],
            "Longitudinal Slope (Inlet)": ["- ≥ 0.005 ft/ft (0.5%)", "- Ensures gutter flow capacity"],
            "Curb Opening Length (ft)": ["- Size to prevent bypass", "- Based on flow and spread"],
            "Gutter Type": ["- Match cross section", "- Consistent with inlet type"],
            "Depressed Gutter": ["- Optional", "- Improves flow capture"],
            "Road Cross Slope (ft/ft)": ["- 2% (0.020) typical", "- Provides positive drainage"],
            "Structure Type": ["- Box structure (precast or cast-in-place)", "- NJDOT standard details"],
            "Elevation (Rim) (ft)": ["- Match finished grade"],
            "Elevation (Invert) (ft)": ["- Invert = Rim - Depth", "- Slope must match pipe"],
            "Rainfall Intensity (in/hr)": ["- 2.5–3.0 per Table 10-2"],
            "Max Spread (ft)": ["- ≤ 6.0 ft (stay out of travel lanes)"],
            "Catch Basin Spacing": ["- Initial: 150 ft", "- Refine by gutter flow/spread"],
            "Headloss Method": ["- HEC-22 Energy"],
            "HEC-22 Benching Method": ["- Flat or Standard"]
        },
        "Pipe": {
            "Conduit Type": ["- Catalog: RCP, PVC, HDPE", "- Use Table 10-4"],
            "Catalog Class / Section Type": ["- Circular for standard use", "- Arched for cover-limited zones"],
            "Diameter / Size": ["- Minimum 15\" for public roads"],
            "Material": ["- RCP under pavements", "- HDPE in non-structural zones"],
            "Manning's n": ["- 0.012–0.015 typical", "- Check Table 10-6"],
            "Invert Start / Stop": ["- Maintain minimum drop", "- Avoid backwater conditions"],
            "Slope": ["- ≥ 0.005 ft/ft preferred", "- Ensure ≥ 2.5 fps velocity"],
            "Length": ["- Based on layout and slope", "- Use scaled or true length"],
            "Is Culvert?": ["- Mark True if inlet control expected", "- Use culvert sizing accordingly"]
        },
        "Manhole": {
            "Update Ground Elevation from Terrain Model?": ["- True if terrain model exists"],
            "Elevation (Ground) (ft)": ["- Match topo or proposed grade"],
            "Set Rim to Ground Elevation?": ["- True unless cover offset needed"],
            "Elevation (Rim) (ft)": ["- Typically equal to ground"],
            "Elevation (Invert) (ft)": ["- Match lowest pipe", "- Add 0.1–0.3 ft drop"],
            "Structure Type": ["- Circular preferred", "- Rectangular for special cases"],
            "Diameter (ft)": ["- ≥ 4 ft for standard pipe sizes"],
            "Bolted Cover?": ["- Required in traffic/flood zones"],
            "Headloss Method": ["- HEC-22 Energy"],
            "HEC-22 Benching Method": ["- Flat or stepped based on flow"]
        },
        "Catchment": {
            "Runoff Method": ["- Rational (< 20 acres)", "- TR-55 for complex/larger areas"],
            "Area Defined By": ["- Single area typical", "- Divide if mixed surfaces"],
            "Runoff Coefficient (Rational)": ["- 0.90 for impervious", "- Use weighted C for mixed cover"],
            "Tc Input Type": ["- User Defined recommended"],
            "Time of Concentration (min)": ["- Minimum 10 minutes (NJDOT)", "- Include all flow segments"]
        },
        "Outfall": {
            "Boundary Condition Type": ["- Free Outfall for open discharge", "- Known tailwater if pond/tidal"],
            "Update Ground Elevation from Terrain Model?": ["- True if using terrain model"],
            "Elevation (Ground) (ft)": ["- Match outlet grading"],
            "Set Rim to Ground Elevation?": ["- True unless offset needed"],
            "Elevation (Invert) (ft)": ["- Match last pipe invert", "- Ensure positive drainage"]
        }
    },

    "NJDOT Bridge & Structures Manual – Section 22": {
        "Inlet": {
            "Inlet Type": ["- Catalog (slot or curb-opening)", "- Place at low points and ends"],
            "Inlet Location": ["- On Grade"],
            "Manning's n (Inlet)": ["- 0.012 (concrete deck)"],
            "Longitudinal Slope (Inlet)": ["- ≥ 0.005 ft/ft preferred"],
            "Curb Opening Length (ft)": ["- Start with 1.0 ft", "- Adjust for spread"],
            "Gutter Type": ["- Standard or custom"],
            "Depressed Gutter": ["- Generally not used on bridges"],
            "Road Cross Slope (ft/ft)": ["- 2% typical deck slope"],
            "Structure Type": ["- Box or slot inlet"],
            "Elevation (Rim) (ft)": ["- Match deck grade"],
            "Elevation (Invert) (ft)": ["- Align with outlet pipe"],
            "Rainfall Intensity (in/hr)": ["- Use 3.0 in/hr"],
            "Max Spread (ft)": ["- ≤ 6.0 ft"],
            "Catch Basin Spacing": ["- Start at 100 ft", "- Confirm via spread analysis"],
            "Headloss Method": ["- HEC-22 Energy"],
            "HEC-22 Benching Method": ["- Flat"]
        },
        "Pipe": {
            "Conduit Type": ["- RCP, VCP"],
            "Catalog Class / Section Type": ["- Circular standard"],
            "Diameter / Size": ["- Size for 10–15 year flow"],
            "Material": ["- Use per structural detail"],
            "Manning's n": ["- 0.011–0.013 typical"],
            "Invert Start / Stop": ["- Align with structure profile"],
            "Slope": ["- ≥ 0.005 ft/ft"],
            "Length": ["- Match bridge layout"],
            "Is Culvert?": ["- True if outlet submerged or inlet control applies"]
        },
        "Manhole": {
            "Update Ground Elevation from Terrain Model?": ["- Optional"],
            "Elevation (Ground) (ft)": ["- Match deck/sidewalk elevation"],
            "Set Rim to Ground Elevation?": ["- True"],
            "Elevation (Rim) (ft)": ["- Match surface"],
            "Elevation (Invert) (ft)": ["- Match pipe invert", "- Maintain slope"],
            "Structure Type": ["- Circular standard"],
            "Diameter (ft)": ["- 4–5 ft standard"],
            "Bolted Cover?": ["- Required on bridge decks"],
            "Headloss Method": ["- HEC-22 Energy"],
            "HEC-22 Benching Method": ["- Flat"]
        },
        "Catchment": {
            "Runoff Method": ["- Rational for small bridge areas"],
            "Area Defined By": ["- Use total bridge deck area"],
            "Runoff Coefficient (Rational)": ["- 0.90 (impervious deck)"],
            "Tc Input Type": ["- User Defined"],
            "Time of Concentration (min)": ["- 10 min typical unless very short deck"]
        },
        "Outfall": {
            "Boundary Condition Type": ["- Free Outfall unless stage control exists"],
            "Update Ground Elevation from Terrain Model?": ["- Optional unless grading linked"],
            "Elevation (Ground) (ft)": ["- Match bridge outlet or abutment slope"],
            "Set Rim to Ground Elevation?": ["- Usually True"],
            "Elevation (Invert) (ft)": ["- Match final pipe outlet invert"]
        }
    }
}

# Streamlit UI
st.set_page_config("NJDOT StormCAD Reference", page_icon="💧")
st.title("🧾 NJDOT StormCAD Field Design Reference")

# Manual & component selector
manual = st.selectbox("📘 Select Manual", manuals.keys())
component = st.radio("📂 Select Component", ["Inlet", "Pipe", "Manhole", "Catchment", "Outfall"])
fields = manuals[manual][component]

# Display interface
st.subheader(f"🛠️ {component} Input Fields – {manual}")
for field, notes in fields.items():
    st.text_area(field, "\n".join(notes), height=100, disabled=True)

st.markdown("---")
st.caption("Values reflect NJDOT drainage standards (Roadway & Bridge Manuals). Use for StormCAD modeling reference.")
