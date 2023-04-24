import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

# Create a sidebar with file upload functionality
st.sidebar.title("Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Main page content
st.title("Interactive Plotting with Vega-Lite")
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

    # Create a scatter plot using Vega-Lite
    chart = alt.Chart(df).mark_circle(size=60).encode(
        x=alt.X(x_axis, type="quantitative", title=x_axis),
        y=alt.Y(y_axis, type="quantitative", title=y_axis),
        color=alt.Color("SEX", type="nominal", title="RACE")
    ).interactive()
    st.altair_chart(chart, use_container_width=True)
