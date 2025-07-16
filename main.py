import streamlit as st
import pandas as pd
import numpy as np

st.title("Demo Dashboard for Posit Connect")

# Example filter
num_points = st.slider("Select number of data points:", min_value=10, max_value=100, value=50)

# Generate example data
df = pd.DataFrame({
    "x": np.arange(num_points),
    "y": np.random.randn(num_points).cumsum()
})

# Chart
st.line_chart(df.set_index("x"))

# Show data table
st.dataframe(df)
