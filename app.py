
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from optimizer import optimize_price  # cloud-safe optimizer

st.set_page_config(page_title="Airbnb Pricing Optimizer", layout="wide")

@st.cache_data
def load_params():
    return pd.read_csv("demand_params.csv")

df_params = load_params()

st.title("🌙 Airbnb Dynamic Pricing Optimizer")
st.markdown("""
This app uses **prescriptive analytics** to recommend the *optimal nightly price*
for an Airbnb listing to maximize monthly revenue.
""")

st.sidebar.header("📌 Select Inputs")

neighbourhood = st.sidebar.selectbox(
    "Neighborhood",
    options=df_params["neighbourhood"].unique()
)

filtered = df_params[df_params["neighbourhood"] == neighbourhood]

if filtered.empty:
    st.error(f"No demand parameters available for {neighbourhood}.")
    st.stop()

row = filtered.iloc[0]
a_default = row["a"]
b_default = row["b"]

p_min = st.sidebar.number_input("Minimum Price ($)", min_value=30, max_value=500, value=50)
p_max = st.sidebar.number_input("Maximum Price ($)", min_value=100, max_value=1000, value=300)

a = st.sidebar.number_input("Demand Intercept (a)", value=float(a_default))
b = st.sidebar.number_input("Price Sensitivity (b)", value=float(b_default))

if st.sidebar.button("Optimize Price"):
    result = optimize_price(p_min, p_max, a, b)

    st.subheader("📊 Optimization Results")
    col1, col2, col3 = st.columns(3)

    col1.metric("Optimal Price", f"${result['optimal_price']}")
    col2.metric("Expected Occupancy", f"{result['optimal_occupancy']}%")
    col3.metric("Projected Monthly Revenue", f"${result['optimal_revenue']}")

    p_vals = np.linspace(p_min, p_max, 200)
    revenue_vals = p_vals * (a - b * p_vals) * 30

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=p_vals, y=revenue_vals,
                             mode="lines",
                             name="Revenue Curve"))
    fig.add_trace(go.Scatter(
        x=[result["optimal_price"]],
        y=[result["optimal_revenue"]],
        mode="markers",
        marker=dict(size=10, color='red'),
        name="Optimal Point"
    ))
    fig.update_layout(
        title="Revenue vs Price",
        xaxis_title="Price ($)",
        yaxis_title="Revenue ($)"
    )
    st.plotly_chart(fig, use_container_width=True)

    demand_vals = a - b * p_vals

    fig2 = go.Figure()
    fig2.add_trace(
        go.Scatter(
            x=p_vals,
            y=demand_vals,
            mode="lines",
            name="Demand Curve"
        )
    )
    fig2.update_layout(
        title="Demand vs Price",
        xaxis_title="Price ($)",
        yaxis_title="Occupancy"
    )

    st.plotly_chart(fig2, use_container_width=True)

else:
    st.info("👈 Use the sidebar to select inputs and click **Optimize Price**.")
