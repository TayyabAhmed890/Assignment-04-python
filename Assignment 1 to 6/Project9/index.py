import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

upload_file = st.file_uploader("Choose a CSV file",type = "csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select Column to filter by",columns)

    unique_values = df[selected_columns].unique()

    selected_values = st.selectbox("Select Value",unique_values)

    filtered_df = df[df[selected_columns] == selected_values]

    st.write(filtered_df)

    st.subheader("Plot Data")
    x_col = st.selectbox("Select X axis Columns",columns)
    y_col = st.selectbox("Select Y axis Columns",columns)

    if st.button("Generate plot"):
        st.line_chart(filtered_df.set_index(x_col)[y_col])

else:
    st.write("Waiting on file upload...")