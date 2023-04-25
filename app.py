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

    # Allow the user to filter the data
    filtered_df = df
    sidebar_selectbox = sidebar.selectbox(
        "Select an option",
        ["No filter", "Filter by column"]
    )
    if sidebar_selectbox == "Filter by column":
        filter_column = st.selectbox("Select Filter Column", columns)
        filter_value = st.text_input("Enter Filter Value")
        if filter_value:
            filtered_df = filtered_df[filtered_df[filter_column] == filter_value]
            if st.button("Clear filter"):
                filtered_df = df

    # Create a stacked bar chart using Plotly
    fig = px.bar(filtered_df, x=x_axis, y=y_axis, color=y_axis, barmode='stack')
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
