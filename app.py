import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import enzyme_yield

st.title("🧪 Virtual Enzyme Production Lab")

st.sidebar.header("Experimental Parameters")

temperature = st.sidebar.slider("Temperature (°C)", 20, 60, 37)
ph = st.sidebar.slider("pH", 3.0, 10.0, 7.0)
substrate = st.sidebar.slider("Substrate Concentration", 0.1, 10.0, 5.0)
time = st.sidebar.slider("Time (hours)", 1, 48, 12)

yield_result = enzyme_yield(temperature, ph, substrate, time)

st.subheader("📊 Enzyme Yield Result")
st.write(f"**Predicted Enzyme Yield:** {yield_result} units")

# Plot yield over time
time_range = np.linspace(1, 48, 100)
yields = [enzyme_yield(temperature, ph, substrate, t) for t in time_range]

fig, ax = plt.subplots()
ax.plot(time_range, yields)
ax.set_xlabel("Time (hours)")
ax.set_ylabel("Enzyme Yield")
ax.set_title("Enzyme Production Over Time")

st.pyplot(fig)