import streamlit as st

# NJDOT manual guidance with page references (no citation tags)
manuals = {
    "NJDOT Roadway Design Manual – Section 10": {
        "Catch Basin": {
            "Inlet Type": [
                "- Curb, grate, or combination inlet per site need (Page 10-43)"
            ],
            "Manning's n (Inlet)": [
                "- Use 0.013 for paved surfaces (Page 10-45)"
            ],
            "Longitudinal Slope (Inlet)": [
                "- Minimum slope = 0.005 ft/ft (Page 10-44)"
            ],
            "Catch Basin Spacing": [
                "- Initial spacing 150 ft; refine based on spread and slope (Page 10-44)"
            ]
        },
        "Pipe Properties": {
            "Conduit Type": [
                "- Use RCP, HDPE, or PVC per Table 10-3 (Page 10-44)"
            ],
            "Diameter / Size": [
                "- Minimum diameter = 15\" (Page 10-44)"
            ],
            "Manning's n": [
                "- 0.012–0.015 typical (Page 10-45)"
            ],
            "Slope": [
                "- Preferred slope ≥ 0.005 ft/ft (Page 10-44)"
            ]
        },
        "Manhole Properties": {
            "Elevation (Invert) (ft)": [
                "- Drop through manhole = 0.1–0.3 ft (Page 10-44)"
            ],
            "Diameter (ft)": [
                "- Minimum 4.0 ft for pipes ≤ 24\" (Page 10-44)"
            ],
            "Structure Type": [
                "- Use circular unless multiple connections (Page 10-44)"
            ]
        },
        "Drainage Area Properties": {
            "Runoff Method": [
                "- Rational Method for areas < 20 acres (Page 10-17)"
            ],
            "Runoff Coefficient (Rational)": [
                "- Use Table 10-2 for C values: 0.3–0.9 (Page 10-19)"
            ],
            "Time of Concentration (min)": [
                "- Minimum Tc = 10 minutes (Page 10-81)"
            ]
        },
        "Outfall Properties": {
            "Outlet Protection": [
                "- Required if velocity > allowable; use NJ Soil Erosion Manual (Page 10-66)"
            ],
            "Boundary Condition Type": [
                "- Assume free outfall unless tailwater elevation known (Page 10-65)"
            ]
        }
    }
}

# UI label mapping
symbology_labels = {
    "Catch Basin": "Catch Basin",
    "Pipe Properties": "Pipe",
    "Manhole Properties": "Manhole",
    "Drainage Area Properties": "Drainage Area",
    "Outfall Properties": "Outfall"
}

# Streamlit App Setup
st.set_page_config("StormCAD Manual Regulations", page_icon="🛠️")
st.title("🧾 StormCAD Manual Regulations")

# Manual & Element UI
manual = st.selectbox("📘 Select Manual", manuals.keys())
element_display = st.radio("📂 Select Element Symbology", list(symbology_labels.values()))
element = next(k for k, v in symbology_labels.items() if v == element_display)
fields = manuals[manual][element]

# Display Guidance
st.subheader(f"🛠️ {element} – {manual}")
for field, bullets in fields.items():
    st.text_area(field, "\n".join(bullets), height=100, disabled=True)

st.markdown("---")
st.caption("All input fields are supported by NJDOT Section 10 references. Page numbers shown in parentheses.")
