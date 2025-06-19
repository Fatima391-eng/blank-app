import streamlit as st

# Bullet-point guidance per field, per manual
manuals = {
    "NJDOT Bridge & Structures Manual – Section 22": {
        "Inlet Type": [
            "- Use slot or curb-opening inlets",
            "- Place at low points and bridge ends",
            "- Must handle 3 in/hr rainfall"
        ],
        "Inlet Location": [
            "- Typically on grade near gutter flowline",
            "- Avoid ponding at sag locations"
        ],
        "Manning's n (Inlet)": [
            "- Use 0.012 for concrete bridge deck surfaces",
            "- Adjust if other materials are used"
        ],
        "Longitudinal Slope (Inlet)": [
            "- Prefer ≥ 0.5% (0.005 ft/ft)",
            "- Minimum 0.3% acceptable for short runs"
        ],
        "Curb Opening Length (ft)": [
            "- Varies with inlet capacity and spread",
            "- Start with 1.0 ft, adjust as needed"
        ],
        "Gutter Type": [
            "- Standard cross-section with uniform slope",
            "- Conventional or custom per bridge geometry"
        ],
        "Depressed Gutter": [
            "- Generally not used on bridges",
            "- Only if hydraulic benefit outweighs risk"
        ],
        "Road Cross Slope (ft/ft)": [
            "- 2% typical bridge deck slope",
            "- Ensures quick runoff collection"
        ],
        "Structure Type": [
            "- Use box or slot-type inlets",
            "- Match with bridge deck detail"
        ],
        "Elevation (Rim) (ft)": [
            "- Match finished bridge deck elevation",
            "- Must not block flow"
        ],
        "Elevation (Invert) (ft)": [
            "- Set per outlet pipe profile",
            "- Avoid negative slope backflow"
        ],
        "Rainfall Intensity (in/hr)": [
            "- Use 3.0 in/hr for inlet spacing design",
            "- Matches NJDOT design storm for bridges"
        ],
        "Max Spread (ft)": [
            "- Maximum allowable: 6.0 ft at curb",
            "- Must not extend into travel lane"
        ],
        "Catch Basin Spacing": [
            "- Start with 100 ft spacing",
            "- Confirm using spread calculations"
        ],
        "Headloss Method": [
            "- HEC-22 Energy Method (3rd Edition)",
            "- Consider entrance, friction, and exit losses"
        ],
        "HEC-22 Benching Method": [
            "- Use Flat benching for NJDOT structures",
            "- Avoid stepped benches unless specified"
        ]
    },

    "NJDOT Roadway Design Manual – Section 10": {
        "Inlet Type": [
            "- Curb, grate, or combination inlet",
            "- Match to site runoff conditions"
        ],
        "Inlet Location": [
            "- Place on grade or in sags",
            "- Locate where gutter flow converges"
        ],
        "Manning's n (Inlet)": [
            "- Use 0.013 for paved surfaces",
            "- Adjust if rougher surface used"
        ],
        "Longitudinal Slope (Inlet)": [
            "- Minimum slope: 0.5% (0.005 ft/ft)",
            "- Needed for gutter and pipe flow"
        ],
        "Curb Opening Length (ft)": [
            "- Dependent on flow and spread",
            "- Size to avoid bypass under design storm"
        ],
        "Gutter Type": [
            "- Defined by roadway cross section",
            "- Consistent with inlet type and location"
        ],
        "Depressed Gutter": [
            "- Optional to improve capture",
            "- Consider if flow bypass risk exists"
        ],
        "Road Cross Slope (ft/ft)": [
            "- Typical: 2% (0.02 ft/ft)",
            "- Must ensure positive drainage"
        ],
        "Structure Type": [
            "- Precast or cast-in-place inlet box",
            "- Must meet structural load requirements"
        ],
        "Elevation (Rim) (ft)": [
            "- Match proposed finished grade",
            "- Prevent tripping or low points"
        ],
        "Elevation (Invert) (ft)": [
            "- Set to align with connecting pipe invert",
            "- Maintain minimum slope for flow"
        ],
        "Rainfall Intensity (in/hr)": [
            "- Use 2.5–3.0 in/hr per region (Table 10-2)",
            "- Check NJDOT rainfall map if unsure"
        ],
        "Max Spread (ft)": [
            "- Must not exceed 6.0 ft at curb",
            "- Spread must stay out of travel lane"
        ],
        "Catch Basin Spacing": [
            "- Start at 150 ft, refine by gutter flow analysis",
            "- Adjust if slope or width varies"
        ],
        "Headloss Method": [
            "- HEC-22 Energy is standard",
            "- Confirm local inlet losses if significant"
        ],
        "HEC-22 Benching Method": [
            "- Flat or standard benching allowed",
            "- Match to structure configuration"
        ]
    }
}

# Streamlit UI
st.set_page_config(page_title="StormCAD Input Guidance", page_icon="🧾")
st.title("🧾 StormCAD Field Guide – NJDOT Design Considerations")

st.markdown("""
Select a manual to view **design-specific guidance** for each StormCAD input field.  
Instead of filling in values, this panel provides **bullet-point recommendations** based on NJDOT standards.
""")

# Manual selector
manual = st.selectbox("📘 Select NJDOT Manual", list(manuals.keys()))
field_data = manuals[manual]

# Inlet input-style panel
st.subheader("🛠️ Inlet Field Panel with Design Notes")
for field, bullets in field_data.items():
    st.text_area(field, "\n".join(bullets), height=100, disabled=True)

st.markdown("---")
st.caption(f"Design considerations are based on: {manual}")
