import streamlit as st
import pandas as pd

# Cleaned data based on your spreadsheet (43 entries per column)
data = {
    "Category": [
        "Design Process Steps", "Design Process Steps", "Design Process Steps", "Design Process Steps", "Design Process Steps", "Design Process Steps",
        "Recurrence Interval", "Recurrence Interval", "Recurrence Interval", "Recurrence Interval", "Recurrence Interval",
        "Hydrologic Methods", "Hydrologic Methods", "Hydrologic Methods",
        "Stormwater Management", "Stormwater Management", "Stormwater Management", "Stormwater Management", "Stormwater Management",
        "Allowable Water Surface Elevation", "Allowable Water Surface Elevation", "Allowable Water Surface Elevation", "Allowable Water Surface Elevation", "Allowable Water Surface Elevation",
        "Drainage Permit Checklist", "Drainage Permit Checklist", "Drainage Permit Checklist", "Drainage Permit Checklist", "Drainage Permit Checklist", "Drainage Permit Checklist",
        "Time of Concentration", "Time of Concentration",
        "Channel Design", "Channel Design", "Channel Design",
        "Stormwater Storage", "Stormwater Storage", "Stormwater Storage", "Stormwater Storage", "Stormwater Storage",
        "Permits & Regulatory Agencies", "Permits & Regulatory Agencies", "Permits & Regulatory Agencies", "Permits & Regulatory Agencies", "Permits & Regulatory Agencies"
    ],
    "Item": [
        "Preliminary Investigation", "Site Analysis", "Choose Recurrence Interval", "Hydrologic Analysis", "Hydraulic Design", "Environmental Review",
        "Freeway/Interstate Cross Drain", "Service Highway Cross Drain", "Longitudinal Pipe – Freeway", "Longitudinal Pipe – Service Hwy", "NJDEP Permit Area",
        "< 20 acres", "< 5 sq mi", "> 1 acre",
        "Water Quantity", "Water Quality", "Recharge", "Nonstructural BMPs First", "Permit Required?",
        "Residence", "Culvert (new)", "Culvert (existing)", "Channel", "Storm Sewer Grate/Rim",
        "Existing Pipes Cleaned", "No Watershed Diversion", "Outfall Protection", "BMPs on Developer Property", "Drainage Calcs Submitted", "ROW and Inlets Shown",
        "Minimum Tc = 10 mins", "Flow Types (sheet, gutter, pipe, channel)",
        "Grassed Channel", "Non-erodible Channel", "Permitting Considerations",
        "Detention Basin", "Retention Basin", "Outlet Design (Weir/Orifice)", "Modeling Tools", "Design Tip",
        "NJDEP FHACA Permit", "Soil Erosion & Sediment Control", "NJPDES Permit", "Pinelands/Highlands/CAFRA", "Category 1 Waters (C1)"
    ],
    "Details": []
        "Gather map"
