import streamlit as st
import pandas as pd
import altair as alt

# Set page configuration
st.set_page_config(layout="wide")

# Create a sidebar with file upload functionality
st.sidebar.title("Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Main page content
st.title("Stacked Bar Chart with Vega-Lite")
st.write("Upload a CSV file and select columns to visualize.")

# Load data if a file has been uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Display the raw data table
    st.subheader("Raw Data")
    st.write(df)

    # Allow the user to select columns to visualize
    columns = list(df.columns)
    x_axis = st.selectbox("Select X Axis", columns)
    y_axis = st.selectbox("Select Y Axis", columns)

    # Allow the user to filter the data
    filtered_df = df
    if st.checkbox("Enable Filtering"):
        filter_column = st.selectbox("Select Filter Column", columns)
        filter_value = st.text_input("Enter Filter Value")
        if filter_value:
            filtered_df = filtered_df[filtered_df[filter_column] == filter_value]

    # Create a stacked bar chart using Vega-Lite
    chart = alt.Chart(filtered_df).mark_bar().encode(
        x=alt.X(x_axis, type="ordinal", title=x_axis),
        y=alt.Y("sum()", title="SUM"),
        color=alt.Color(y_axis, type="nominal", title=y_axis)
    ).properties(
        width=700,
        height=500
    )

    st.altair_chart(chart, use_container_width=True)
