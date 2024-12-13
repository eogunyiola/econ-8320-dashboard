
import streamlit as st
import pandas as pd

# Loading the data
data = pd.read_csv("labor_statistics.csv")

# Dashboard Title
st.title("US Labor Statistics Dashboard")

# Showing raw data
if st.checkbox("Show raw data"):
    st.write(data)

# Selecting series to plot
selected_series = st.selectbox("Select a series to visualize:", data["series"].unique())

# Filted data for the selected series
filtered_data = data[data["series"] == selected_series]

# Ploting the data
st.line_chart(filtered_data.set_index("date")["value"])
