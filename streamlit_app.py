import streamlit as st

manuals = {
    "NJDOT Roadway Design Manual – Section 10": {
        "Catch Basin": {
            "Inlet Type": ["- Curb, grate, or combination inlet per site need (Page 10-43) \"catch basins are typically...\""],
            "Manning's n (Inlet)": ["- Use 0.013 for paved surfaces (Table 10-4) \"Manning’s roughness coefficients...\""],
            "Longitudinal Slope (Inlet)": ["- Minimum slope = 0.005 ft/ft (Page 10-44) \"minimum gutter slope should...\""],
            "Catch Basin Spacing": ["- Start at 150 ft; refine by slope/spread (Page 10-44) \"spacing between inlets is typically...\""]
        },
        "Pipe Properties": {
            "Conduit Type": ["- Use RCP, HDPE, or PVC (Page 10-44) \"culverts and storm drains must...\""],
            "Diameter / Size": ["- Minimum diameter = 15\" (Page 10-44) \"minimum pipe size is...\""],
            "Manning's n": ["- 0.012–0.015 typical (Table 10-4) \"Manning’s roughness coefficients...\""],
            "Slope": ["- Preferred slope ≥ 0.005 ft/ft (Page 10-44) \"minimum gutter slope should...\""]
        },
        "Manhole Properties": {
            "Elevation (Invert) (ft)": ["- Provide 0.1–0.3 ft drop across manhole (Page 10-44) \"a drop of 0.1 to 0.3...\""],
            "Structure Type": ["- Use circular unless multiple connections (Page 10-44) \"manholes are typically circular...\""],
            "Diameter (ft)": ["- Minimum 4.0 ft for access (Page 10-44) \"minimum manhole diameter is...\""]
        },
        "Drainage Area Properties": {
            "Runoff Method": ["- Rational Method if < 20 acres (Page 10-17) \"for drainage areas less than...\""],
            "Runoff Coefficient (Rational)": ["- Use C from 0.30–0.90 (Table 10-2) \"Runoff coefficients for typical...\""],
            "Time of Concentration (min)": ["- Minimum Tc = 10 minutes (Page 10-81) \"minimum time of concentration...\""]
        },
        "Outfall Properties": {
            "Boundary Condition Type": ["- Assume free outfall unless tailwater exists (Page 10-65) \"free outfall conditions are...\""],
            "Outlet Protection": ["- Required when velocity exceeds limits (Page 10-66) \"velocity dissipation must be...\""]
        }
    },

    "NJDOT Bridge & Structures Manual – Section 22": {
        "Catch Basin": {
            "Inlet Type": ["- Use bridge deck drains or scuppers (Page 22-10) \"bridge deck drainage inlets...\""],
            "Manning's n (Inlet)": ["- Use 0.012 for concrete (Page 22-12) \"roughness coefficient of 0.012...\""],
            "Road Cross Slope (ft/ft)": ["- Typical deck slope = 2% (Page 22-5) \"a cross slope of 2 percent...\""],
            "Catch Basin Spacing": ["- Initial spacing ≈ 100 ft (Page 22-13) \"spacing of inlets on bridge...\""]
        },
        "Pipe Properties": {
            "Diameter / Size": ["- Design for 10–15 year storm (Page 22-11) \"storm drain design shall be...\""],
            "Manning's n": ["- Use 0.012 for RCP/CMP (Page 22-12) \"roughness coefficient of 0.012...\""],
            "Slope": ["- Preferred slope ≥ 0.005 ft/ft (Page 22-11) \"a minimum slope of 0.005...\""]
        },
        "Manhole Properties": {
            "Structure Type": ["- Use circular unless space-limited (Page 22-14) \"circular manholes are preferred...\""],
            "Diameter (ft)": ["- Minimum 4 ft inside diameter (Page 22-14) \"minimum diameter should be...\""]
        },
        "Drainage Area Properties": {
            "Runoff Method": ["- Use Rational Method (Page 22-8) \"rational method shall be used...\""],
            "Runoff Coefficient (Rational)": ["- Use C = 0.90 for bridge deck (Page 22-8) \"for bridge deck areas...\""],
            "Time of Concentration (min)": ["- Minimum Tc = 10 min (Page 22-8) \"a minimum Tc of 10 minutes...\""]
        },
        "Outfall Properties": {
            "Boundary Condition Type": ["- Free outfall unless staged (Page 22-15) \"free outfall is assumed...\""],
            "Outlet Protection": ["- Use riprap, flared ends, or guide walls (Page 22-15) \"provide appropriate protection...\""]
        }
    },

    "HDS-4: Introduction to Highway Hydraulics (FHWA-NHI-08-090)": {
        "Catch Basin": {
            "Inlet Type": ["- Use flared/headwall to reduce erosion (Page 118) \"headwalls and flared end...\""],
            "Grate Type": ["- Use non-bendable grate types (Page 118) \"grate inlets should be...\""],
            "Inlet Location": ["- Align with roadway drainage path (Page 113) \"drainage area topography must...\""],
            "Capture Efficiency": ["- Partial capture depends on Tc and slope (Page 114) \"peak runoff may not occur...\""]
        },
        "Pipe Properties": {
            "Material": ["- Use RCP or CMP per spec (Page 95) \"culverts may be constructed...\""],
            "Diameter": ["- Size pipe using HY-8 or nomographs (Page 97) \"hydraulic design of culverts...\""],
            "Slope": ["- Match natural grade if feasible (Page 97) \"culvert slope should match...\""],
            "Roughness (Manning's n)": ["- Use n = 0.012–0.025 (Page B-3) \"Manning's n values for...\""],
            "Design Flow": ["- Use peak subarea if it exceeds total (Page 114) \"a subarea with a shorter...\""]
        },
        "Manhole Properties": {
            "Invert Elevation": ["- Match in/out for flow (Page 97) \"match inlet and outlet elevations...\""],
            "Number of Pipes": ["- Confirm inflow and losses (Page 118) \"consider energy losses when...\""]
        },
        "Drainage Area Properties": {
            "Area": ["- Delineate with topo or aerial (Page 113) \"delineate drainage areas using...\""],
            "Runoff Coefficient (C)": ["- C = 0.30–0.90 by land use (Page B-1) \"runoff coefficients by land...\""],
            "Time of Concentration": ["- Use McCuen formula (Page 113) \"McCuen equation is recommended...\""],
            "Rainfall Intensity": ["- Use IDF or NOAA Atlas 14 (Page 114) \"determine intensity from IDF...\""]
        },
        "Outfall Properties": {
            "Tailwater Condition": ["- Base on downstream control (Page 97) \"tailwater may control outlet...\""],
            "Energy Dissipator": ["- Use if velocity > 10 ft/s (Page 118) \"energy dissipation is needed...\""],
            "Outlet Protection": ["- Use riprap or plunge pool (Page 118) \"riprap or basin may be...\""]
        }
    }
}

# StormCAD terminology for UI
symbology_labels = {
    "Catch Basin": "Catch Basin",
    "Pipe Properties": "Pipe",
    "Manhole Properties": "Manhole",
    "Drainage Area Properties": "Drainage Area",
    "Outfall Properties": "Outfall"
}

# Streamlit app UI
st.set_page_config("StormCAD Manual Regulations", page_icon="🛠️")
st.title("🧾 StormCAD Manual Regulations")

# Manual + Element Dropdowns
manual = st.selectbox("📘 Select Manual", manuals.keys())
element_display = st.radio("📂 Select Element Symbology", list(symbology_labels.values()))
element = next(k for k, v in symbology_labels.items() if v == element_display)
fields = manuals[manual][element]

# Display guidance per field
st.subheader(f"🛠️ {element} – {manual}")
for field, bullets in fields.items():
    st.text_area(field, "\n".join(bullets), height=100, disabled=True)

st.markdown("---")
st.caption("Manual-derived input values with page references and quoted text for Ctrl+F search.")
