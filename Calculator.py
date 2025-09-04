import streamlit as st
import pandas as pd

st.set_page_config(page_title="Solar Planner", page_icon="☀️")

st.title("☀️ Solar Energy Planner")
st.write("Calculate your potential solar energy generation and savings.")

# Inputs
st.header("Enter Your Details")
roof_size = st.slider("Roof Size (sq meters)", 10, 200, 50)
sunlight_hours = st.slider("Average Sunlight Hours per Day", 1, 12, 5)
electricity_rate = st.slider("Electricity Rate (per kWh in $)", 0.05, 0.50, 0.15)

# Calculation
solar_yield = roof_size * 0.15 * sunlight_hours  # 0.15 kW per sqm
daily_production = solar_yield
annual_production = daily_production * 365
annual_savings = annual_production * electricity_rate

# Display Results
st.header("Results")
st.metric("Estimated Daily Production", f"{daily_production:.2f} kWh")
st.metric("Estimated Annual Production", f"{annual_production:.2f} kWh")
st.metric("Estimated Annual Savings", f"${annual_savings:.2f}")

st.info("Note: This is a simplified estimate. Real-world factors may vary.")
