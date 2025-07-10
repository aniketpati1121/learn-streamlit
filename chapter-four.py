import streamlit as st
import pandas as pd 

st.title("Chai Sales Data Analysis")

file = st.file_uploader("Upload your CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df) 

if file:
    st.subheader("Summary Statistics")  
    st.write(df.describe()) 

if file:
    CITIES = df['City'].unique()
    selected_city = st.selectbox("Select a City to filter data:", CITIES)
    filtered_data = df["City"] == selected_city  # Ensure 'City' is treated as a string
    st.dataframe(df[filtered_data])