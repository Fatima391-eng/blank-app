import streamlit as st

# Manual-based field guidance with page references
manuals = {
    "NJDOT Roadway Design Manual – Section 10": {
        "Catch Basin": {
            "Inlet Type": [
                "- Curb, grate, or combination inlet per site need (Sec 10.6.1) (Page 10-43):contentReference[oaicite:0]{index=0}"
            ],
            "Manning's n (Inlet)": [
                "- Use 0.013 for paved surfaces (Table 10-4) (Page 10-45):contentReference[oaicite:1]{index=1}"
            ],
            "Longitudinal Slope (Inlet)": [
                "- Minimum slope = 0.005 ft/ft (Sec 10.6.1) (Page 10-44):contentReference[oaicite:2]{index=2}"
            ],
            "Catch Basin Spacing": [
                "- Initial spacing 150 ft; refine based on spread and slope (Sec 10.6.1) (Page 10-44):contentReference[oaicite:3]{index=3}"
            ]
        },
        "Pipe Properties": {
            "Conduit Type": [
                "- Use RCP, HDPE, or PVC per Table 10-3 (Page 10-44):contentReference[oaicite:4]{index=4}"
            ],
            "Diameter / Size": [
                "- Minimum diameter = 15\" (Sec 10.6.1) (Page 10-44):contentReference[oaicite:5]{index=5}"
            ],
            "Manning's n": [
                "- 0.012–0.015 typical (Table 10-4) (Page 10-45):contentReference[oaicite:6]{index=6}"
            ],
            "Slope": [
                "- Preferred slope ≥ 0.005 ft/ft (Sec 10.6.1) (Page 10-44):contentReference[oaicite:7]{index=7}"
            ]
        },
        "Manhole Properties": {
            "Elevation (Invert) (ft)": [
                "- Drop through manhole = 0.1–0.3 ft (Sec 10.6.1) (Page 10-44):contentReference[oaicite:8]{index=8}"
            ],
            "Diameter (ft)": [
                "- Minimum 4.0 ft for pipes ≤ 24\" (Sec 10.6.1) (Page 10-44):contentReference[oaicite:9]{index=9}"
            ],
            "Structure Type": [
                "- Use circular unless multiple connections (Sec 10.6.1) (Page 10-44):contentReference[oaicite:10]{index=10}"
            ]
        },
        "Drainage Area Properties": {
            "Runoff Method": [
                "- Rational Method for areas < 20 acres (Sec 10.5.1) (Page 10-17):contentReference[oaicite:11]{index=11}"
            ],
            "Runoff Coefficient (Rational)": [
                "- Use Table 10-2 for C values: 0.3–0.9 (Page 10-19):contentReference[oaicite:12]{index=12}"
            ],
            "Time of Concentration (min)": [
                "- Minimum Tc = 10 minutes (Sec 10.5.3) (Page 10-81):contentReference[oaicite:13]{index=13}"
            ]
        },
        "Outfall Properties": {
            "Outlet Protection": [
                "- Required if velocity > allowable; use NJ Soil Erosion Manual (Sec 10.7.2) (Page 10-66):contentReference[oaicite:14]{index=14}"
            ],
            "Boundary Condition Type": [
                "- Assume free outfall unless tailwater elevation known (Sec 10.7.1) (Page 10-65):contentReference[oaicite:15]{index=15}"
            ]
        }
    }
}

# Label mapping (for UI)
symbology_labels = {
    "Catch Basin": "Catch Basin",
    "Pipe Properties": "Pipe",
    "Manhole Properties": "Manhole",
    "Drainage Area Properties": "Drainage Area",
    "Outfall Properties": "Outfall"
}

# Streamlit Setup
st.set_page_config("StormCAD Manual Regulations", page_icon="🛠️")
st.title("🧾 StormCAD Manual Regulations")

# UI Controls
manual = st.selectbox("📘 Select Manual", manuals.keys())
element_display = st.radio("📂 Select Element Symbology", list(symbology_labels.values()))
element = next(k for k, v in symbology_labels.items() if v == element_display)
fields = manuals[manual][element]

# Display field guidance with citations
st.subheader(f"🛠️ {element} – {manual}")
for field, notes in fields.items():
    st.text_area(field, "\n".join(notes), height=100, disabled=True)

st.markdown("---")
st.caption("All input fields are supported by NJDOT Section 10 references with page numbers.")
