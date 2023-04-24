import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

# Create a sidebar with file upload functionality
st.sidebar.title("Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Main page content
st.title("Interactive Plotting with Altair")
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

    # Allow the user to select a filter column
    filter_columns = [col for col in columns if col != x_axis and col != y_axis]
    filter_dropdown = st.selectbox("Select Filter", filter_columns, index=len(filter_columns))

    # Allow the user to select a filter value
    filter_values = sorted(df[filter_dropdown].unique())
    filter_values.insert(0, "All")
    filter_value = st.selectbox("Select Value", filter_values)

    # Filter the data based on the user selection
    if filter_value != "All":
        df = df[df[filter_dropdown] == filter_value]

    # Create a stacked bar chart using Altair
    chart = alt.Chart(df).mark_bar().encode(
        x=x_axis,
        y=alt.Y("sum({})".format(y_axis), stack=None),
        color=alt.Color(filter_dropdown, type="nominal", title=filter_dropdown),
        tooltip=[x_axis, alt.Tooltip("sum({})".format(y_axis), title=y_axis)]
    ).properties(
        width=800,
        height=600
    )

    # Display the chart
    st.altair_chart(chart, use_container_width=True)
