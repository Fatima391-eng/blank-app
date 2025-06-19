import streamlit as st
import pandas as pd

data = {
    "Category": ["Design Process Steps", "Stormwater Management"],
    "Item": ["Site Analysis", "Water Quantity"],
    "Details": [
        "Assess drainage area, soils, slope, permits",
        "Prevent increase in peak discharge and volume"
    ]
}
df = pd.DataFrame(data)

st.set_page_config(page_title="NJ Drainage Tool", page_icon="💧")
st.title("💧 NJ Drainage Design Lookup Tool")

category = st.selectbox("1. Choose a Category", sorted(df["Category"].unique()))
filtered = df[df["Category"] == category]
item = st.selectbox("2. Choose an Item", filtered["Item"])
detail = filtered[filtered["Item"] == item]["Details"].values[0]

st.markdown("### 3. Design Guidance:")
st.success(detail)
