import streamlit as st
import pyperclip

# StormCAD-ready inputs with units
manuals = {
    "NJDOT Roadway Design Manual – Section 10": {
        "Pipe Design": (
            "**Design Storm:** 10-year (Service Roads), 15-year (Freeways)\n"
            "**Method:** Rational (< 20 acres) or TR-55 (< 5 sq mi)\n"
            "**Use in StormCAD:** Set inlet catchment area, design storm, and flow method accordingly"
        ),
        "Time of Concentration": (
            "**Minimum Tc:** 10 minutes\n"
            "**Include:** Sheet flow, shallow flow, pipe/channel flow\n"
            "**Use in StormCAD:** Tc ≥ 10 min required in gutter and junction hydrology settings"
        ),
        "Outlet Structure": (
            "**Orifice Formula:** Q = CA(2gH)^0.5\n"
            "**Weir Formula:** Q = CLH^1.5\n"
            "**Use in StormCAD:** Use outlet control structure editor for weir/orifice rating curves"
        ),
        "Quantity Control": (
            "**Peak Flow Control:** Match or reduce pre-development flows\n"
            "**Events:** 2-, 10-, 25-, 100-year storms\n"
            "**Use in StormCAD:** Detention pond or outlet structure flow balancing"
        ),
        "Culvert Sizing": (
            "**Design Storm:** 25-year (Service Road), 50-year (Interstate)\n"
            "**Allowable Headwater:** No overtopping\n"
            "**Use in StormCAD:** Culvert entrance control; size based on design storm"
        )
    },

    "NJDOT Bridge & Structures Manual – Section 22": {
        "Bridge Deck Inlet Setup (StormCAD)": (
            "**Inlet Type:** Catalog (e.g., 3\" x 12\" slot drain)\n"
            "**Inlet Location:** On Grade\n"
            "**Manning's n (Inlet):** 0.012\n"
            "**Longitudinal Slope:** 1.2% (0.012)\n"
            "**Curb Opening Length:** 1.0 ft\n"
            "**Cross Slope (Deck):** 2% (0.02)\n"
            "**Gutter Type:** User Defined – Conventional\n"
            "**Depressed Gutter:** False\n"
            "**Elevation (Rim):** ~111.87 ft\n"
            "**Elevation (Invert):** Set per profile"
        ),
        "Gutter and Spread Criteria": (
            "**Rainfall Intensity:** 3 in/hr\n"
            "**Max Spread:** 6.0 ft\n"
            "**Manning’s n (Gutter):** 0.012\n"
            "**Use in StormCAD:** Set in gutter geometry and inlet capture settings"
        ),
        "Catch Basin Placement Guidance": (
            "**Location:** Low points, sag curves, bridge ends\n"
            "**Max Spacing:** Start with 100 ft, refine with spread analysis\n"
            "**No ponding in travel lanes under design storm**"
        )
    }
}

# App setup
st.set_page_config(page_title="StormCAD Drainage Input Helper", page_icon="💧")
st.title("💧 NJDOT StormCAD Drainage Input Helper")

# Description
st.markdown("""
Use this tool to get StormCAD-ready drainage and inlet design values directly from NJDOT manuals.  
Select the relevant manual and design task, and you’ll get copy-paste values, units, and modeling notes.
""")

# Manual + task dropdowns
selected_manual = st.selectbox("Select a Manual", list(manuals.keys()))
selected_topic = st.selectbox("Select a Design Task", list(manuals[selected_manual].keys()))

# Output
guidance = manuals[selected_manual][selected_topic]
st.markdown("### Design Inputs:")
st.markdown(guidance)

# Optional copy button (informational)
st.text("Copy the above to use in StormCAD or CivilStorm.")

# Footer
st.markdown("---")
st.caption("NJDOT Roadway Manual (Sec 10) & Bridge Manual (Sec 22) | Adapted for StormCAD usage")
