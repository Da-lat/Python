import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

upload_file = st.file_uploader("Choose a CSV file", type="csv")

if upload_file is not None:
    st.write("File Uploaded Successfully")
    df = pd.read_csv(upload_file)

    st.subheader("Data Preview")
    st.write(df.head(10))

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter by", columns)

    unique_values = df[selected_column].unique().tolist()
    selected_value = st.selectbox("Select a value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]

    st.subheader("Filtered Data")
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select the x-axis column", columns)
    y_column = st.selectbox("Select the y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Waiting on file upload...")