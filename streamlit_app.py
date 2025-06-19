import streamlit as st

manuals = {
    "NJDOT Roadway Design Manual – Section 10": {
        "Catch Basin": {
            "Inlet Type": ["- Curb, grate, or combination inlet per site need (Page 10-43)"],
            "Manning's n (Inlet)": ["- Use 0.013 for paved surfaces (Page 10-45)"],
            "Longitudinal Slope (Inlet)": ["- Minimum slope = 0.005 ft/ft (Page 10-44)"],
            "Catch Basin Spacing": ["- Start at 150 ft; refine by slope/spread (Page 10-44)"]
        },
        "Pipe Properties": {
            "Conduit Type": ["- Use RCP, HDPE, or PVC (Page 10-44)"],
            "Diameter / Size": ["- Minimum diameter = 15\" (Page 10-44)"],
            "Manning's n": ["- 0.012–0.015 typical (Page 10-45)"],
            "Slope": ["- Preferred slope ≥ 0.005 ft/ft (Page 10-44)"]
        },
        "Manhole Properties": {
            "Elevation (Invert) (ft)": ["- Provide 0.1–0.3 ft drop across manhole (Page 10-44)"],
            "Structure Type": ["- Use circular unless multiple connections (Page 10-44)"],
            "Diameter (ft)": ["- Minimum 4.0 ft for access (Page 10-44)"]
        },
        "Drainage Area Properties": {
            "Runoff Method": ["- Rational Method if < 20 acres (Page 10-17)"],
            "Runoff Coefficient (Rational)": ["- Use Table 10-2: 0.30–0.90 range (Page 10-19)"],
            "Time of Concentration (min)": ["- Minimum Tc = 10 minutes (Page 10-81)"]
        },
        "Outfall Properties": {
            "Boundary Condition Type": ["- Assume free outfall unless tailwater exists (Page 10-65)"],
            "Outlet Protection": ["- Required when velocity exceeds limits (Page 10-66)"]
        }
    },

    "NJDOT Bridge & Structures Manual – Section 22": {
        "Catch Basin": {
            "Inlet Type": ["- Use bridge deck drains or scuppers as appropriate (Page 22-10)"],
            "Manning's n (Inlet)": ["- Use 0.012 for concrete deck (Page 22-12)"],
            "Road Cross Slope (ft/ft)": ["- Typical deck slope = 2% (Page 22-5)"],
            "Catch Basin Spacing": ["- Initial spacing ≈ 100 ft; refine based on spread (Page 22-13)"]
        },
        "Pipe Properties": {
            "Diameter / Size": ["- Design for 10–15 year storm (Page 22-11)"],
            "Manning's n": ["- Use 0.012 for RCP/CMP (Page 22-12)"],
            "Slope": ["- Preferred slope ≥ 0.005 ft/ft (Page 22-11)"]
        },
        "Manhole Properties": {
            "Structure Type": ["- Use circular manholes unless space-limited (Page 22-14)"],
            "Diameter (ft)": ["- 4 ft minimum inside diameter (Page 22-14)"]
        },
        "Drainage Area Properties": {
            "Runoff Method": ["- Rational Method for deck drainage (Page 22-8)"],
            "Runoff Coefficient (Rational)": ["- Use C = 0.90 for concrete bridge deck (Page 22-8)"],
            "Time of Concentration (min)": ["- Use minimum Tc = 10 min unless short travel time (Page 22-8)"]
        },
        "Outfall Properties": {
            "Boundary Condition Type": ["- Free outfall unless tied to stage elevation (Page 22-15)"],
            "Outlet Protection": ["- Use riprap, flared end sections, or guide walls (Page 22-15)"]
        }
    },

    "HDS-4: Introduction to Highway Hydraulics (FHWA-NHI-08-090)": {
        "Catch Basin": {
            "Inlet Type": ["- Use flared or headwall inlets to reduce erosion (Page 118)"],
            "Grate Type": ["- Use strong, non-bendable grate materials (Page 118)"],
            "Inlet Location": ["- Align with roadway grade and flow (Page 113)"],
            "Capture Efficiency": ["- Partial capture depends on Tc and slope (Page 114)"]
        },
        "Pipe Properties": {
            "Material": ["- Use RCP or CMP; check local specs (Page 95)"],
            "Diameter": ["- Size pipe using nomographs or HY-8 (Page 97)"],
            "Slope": ["- Match natural slope where possible (Page 97)"],
            "Roughness (Manning's n)": ["- n = 0.012–0.025 typical (Page B-3)"],
            "Design Flow": ["- Use peak subarea runoff if higher than total (Page 114)"]
        },
        "Manhole Properties": {
            "Invert Elevation": ["- Maintain hydraulic slope through structure (Page 97)"],
            "Number of Pipes": ["- Confirm cumulative inflow and energy loss (Page 118)"]
        },
        "Drainage Area Properties": {
            "Area": ["- Measure using topo or aerial survey (Page 113)"],
            "Runoff Coefficient (C)": ["- Use 0.30–0.90 based on surface (Page B-1)"],
            "Time of Concentration": ["- Use McCuen’s equation for overland flow (Page 113)"],
            "Rainfall Intensity": ["- Use IDF or NOAA Atlas 14 (Page 114)"]
        },
        "Outfall Properties": {
            "Tailwater Condition": ["- Estimate based on downstream control (Page 97)"],
            "Energy Dissipator": ["- Required if outlet velocity > 10 ft/s (Page 118)"],
            "Outlet Protection": ["- Use riprap or plunge pool where needed (Page 118)"]
        }
    }
}

# Label mapping for display
symbology_labels = {
    "Catch Basin": "Catch Basin",
    "Pipe Properties": "Pipe",
    "Manhole Properties": "Manhole",
    "Drainage Area Properties": "Drainage Area",
    "Outfall Properties": "Outfall"
}

# App config
st.set_page_config("StormCAD Manual Regulations", page_icon="🛠️")
st.title("🧾 StormCAD Manual Regulations")

# Dropdowns
manual = st.selectbox("📘 Select Manual", manuals.keys())
element_display = st.radio("📂 Select Element Symbology", list(symbology_labels.values()))
element = next(k for k, v in symbology_labels.items() if v == element_display)
fields = manuals[manual][element]

# Display
st.subheader(f"🛠️ {element} – {manual}")
for field, bullets in fields.items():
    st.text_area(field, "\n".join(bullets), height=100, disabled=True)

st.markdown("---")
st.caption("All input fields come from official manuals. Page numbers shown in parentheses.")
