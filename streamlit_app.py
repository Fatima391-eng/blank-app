import streamlit as st

# StormCAD design considerations per manual
manuals = {
    "NJDOT Bridge & Structures Manual – Section 22": {
        "Inlet": {
            "Inlet Type": [
                "- Use slot or curb-opening inlets",
                "- Place at low points and bridge ends"
            ],
            "Inlet Location": [
                "- Typically on grade near gutter flowline",
                "- Avoid sag without proper capture"
            ],
            # ... other inlet fields as before ...
        },
        "Pipe": {
            "Conduit Type": [
                "- Catalog conduit (e.g., RCP, HDPE)",
                "- Follow standard NJDOT drainage details"
            ],
            "Catalog Class / Section Type": [
                "- Circle for standard pipes",
                "- Use box for short culvert-like spans"
            ],
            "Diameter / Size": [
                "- Minimum 15\" for cross drains",
                "- Check capacity for 10- or 15-year flow"
            ],
            "Material": [
                "- RCP for road crossings",
                "- HDPE or VCP in select non-structural zones"
            ],
            "Manning's n": [
                "- 0.013 for RCP",
                "- 0.011 for VCP",
                "- 0.012–0.015 range typical"
            ],
            "Invert Start / Stop": [
                "- Set based on slope and drop inlet",
                "- Ensure min velocity of 2.5 fps"
            ],
            "Slope": [
                "- 0.5% minimum preferred",
                "- Must prevent sediment deposition"
            ],
            "Length": [
                "- Match roadway layout and structure spacing",
                "- Use scaled or calculated length in StormCAD"
            ],
            "Is Culvert?": [
                "- True if flowing full under inlet control",
                "- Otherwise use pipe hydraulics"
            ]
        }
    },
    "NJDOT Roadway Design Manual – Section 10": {
        "Inlet": {
            # Same inlet fields as before...
        },
        "Pipe": {
            "Conduit Type": [
                "- Use RCP, PVC, or HDPE per Table 10-4",
                "- Follow standard NJDOT material specs"
            ],
            "Catalog Class / Section Type": [
                "- Circular for typical drainage pipes",
                "- Arched or elliptical for flat cover zones"
            ],
            "Diameter / Size": [
                "- 15\" minimum for public roads",
                "- Confirm flow capacity using Rational Q"
            ],
            "Material": [
                "- RCP preferred under pavement",
                "- HDPE in grassed or rear yard systems"
            ],
            "Manning's n": [
                "- 0.012–0.015 typical",
                "- Confirm per manufacturer or Table 10-6"
            ],
            "Invert Start / Stop": [
                "- Use minimum 0.5 ft drop if possible",
                "- Prevent backup from outlet"
            ],
            "Slope": [
                "- Minimum slope 0.005 ft/ft (0.5%)",
                "- Adjust to meet velocity ≥ 2.5 fps"
            ],
            "Length": [
                "- Based on horizontal layout",
                "- Use true or scaled field length"
            ],
            "Is Culvert?": [
                "- Use culvert calc if subject to ponding",
                "- Pipe calc valid for open outlet conditions"
            ]
        }
    }
}

# App UI
st.set_page_config("StormCAD Field Panel", page_icon="💧")
st.title("🧾 NJDOT StormCAD Input Field Guide")

# Manual selection
selected_manual = st.selectbox("Select Manual", manuals.keys())
component_type = st.radio("Select Component", ["Inlet", "Pipe"])
field_data = manuals[selected_manual][component_type]

# Show form panel
st.subheader(f"🛠️ {component_type} Field Panel – {selected_manual}")
for field, bullets in field_data.items():
    st.text_area(field, "\n".join(bullets), height=100, disabled=True)

st.markdown("---")
st.caption(f"Design considerations are based on: {selected_manual} | Section: {'22' if 'Bridge' in selected_manual else '10'}")
