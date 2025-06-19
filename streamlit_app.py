import streamlit as st

# Pre-filled values for StormCAD input fields from NJDOT manuals
manuals = {
    "NJDOT Bridge & Structures Manual – Section 22": {
        "Inlet Type": "Catalog – 3\" x 12\" Slot Drain",
        "Inlet Location": "On Grade",
        "Manning's n (Inlet)": "0.012",
        "Longitudinal Slope (Inlet)": "0.012",
        "Curb Opening Length (ft)": "1.0",
        "Gutter Type": "User Defined – Conventional",
        "Depressed Gutter": "False",
        "Road Cross Slope (ft/ft)": "0.020 (2%)",
        "Structure Type": "Box Structure",
        "Elevation (Rim) (ft)": "~111.87 ft (match deck profile)",
        "Elevation (Invert) (ft)": "Set per outlet pipe design",
        "Rainfall Intensity (in/hr)": "3.0",
        "Max Spread (ft)": "6.0",
        "Catch Basin Spacing": "Start with 100 ft, refine by spread analysis",
        "Headloss Method": "HEC-22 Energy (3rd Edition)",
        "HEC-22 Benching Method": "Flat"
    },
    "NJDOT Roadway De
