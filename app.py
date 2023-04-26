import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(layout="wide")

# Create a sidebar with file upload functionality
sidebar = st.sidebar
sidebar.title("Upload CSV")
uploaded_file = sidebar.file_uploader("Choose a CSV file", type="csv")

# Main page content
st.title("Stacked Bar Chart with Plotly")
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

    # Create a stacked bar chart using Plotly
    fig = px.bar(df, x=x_axis, y=y_axis, color=y_axis, barmode='stack')
    fig.update_layout(
        width=700,
        height=500,
        drillmode="select"
    )
    fig.update_traces(texttemplate='%{text:.2s}', textposition='auto')
    fig.update_layout(
        title={
            'text': "Stacked Bar Chart with Plotly",
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis_title=x_axis,
        yaxis_title="Sum"
    )

    st.plotly_chart(fig, use_container_width=True)
