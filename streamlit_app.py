import streamlit as st

# Structured field-by-field StormCAD input template
stormcad_fields = {
    "Inlet Type": "Catalog – 3\" x 12\" Slot Drain",
    "Inlet Location": "On Grade",
    "Manning's n (Inlet)": "0.012",
    "Longitudinal Slope (Inlet)": "0.012",
    "Curb Opening Length (ft)": "1.0",
    "Gutter Type": "User Defined – Conventional",
    "Depressed Gutter": "False",
    "Road Cross Slope (ft/ft)": "0.020 (2%)",
    "Structure Type": "Box Structure",
    "Elevation (Rim)": "~111.87 ft (match deck profile)",
    "Elevation (Invert)": "Set per outlet pipe",
    "Rainfall Intensity (in/hr)": "3.0",
    "Max Spread (ft)": "6.0",
    "Catch Basin Spacing": "Start with 100 ft, refine by spread analysis",
    "Headloss Method": "HEC-22 Energy (3rd Edition)",
    "HEC-22 Benching Method": "Flat"
}

# App config
st.set_page_config(page_title="StormCAD Input Field Guide", page_icon="🧾")
st.title("🧾 StormCAD Inlet Design Input – NJDOT Recommended Values")

st.markdown("""
This guide shows NJDOT-recommended field values for inlet setup in **StormCAD** based on the **Bridge Manual Section 22**.  
Use it as a reference for modeling inlets, gutters, and pipe tie-ins. Values are based on NJDOT standard practice for bridge drainage.
""")

# Show input-style layout
st.markdown("### Input Fields with NJDOT Recommendations")
for field, recommendation in stormcad_fields.items():
    st.text_input(label=field, value=recommendation, disabled=True)

st.markdown("---")
st.caption("Values sourced from NJDOT Bridge & Structures Manual – Section 22 and field modeling standards.")
