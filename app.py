import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    """
    Streamlit app for visualizing CSV and Excel files using Plotly.
    """
    st.title("Data Visualization App")

    # File upload
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            # Read the file based on its extension
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
            else:
                st.error("Unsupported file type. Please upload CSV or Excel.")
                return

            # Display the DataFrame
            st.dataframe(df)

            # Select columns for visualization
            x_col = st.selectbox("Select X-axis column", options=df.columns)
            y_col = st.selectbox("Select Y-axis column", options=df.columns)

            # Select plot type
            plot_type = st.selectbox("Select Plot Type", 
                                    options=["Scatter", "Line", "Bar", "Histogram"])

            # Create the Plotly figure based on the selected plot type
            if plot_type == "Scatter":
                fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
            elif plot_type == "Line":
                fig = px.line(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
            elif plot_type == "Bar":
                fig = px.bar(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
            elif plot_type == "Histogram":
                fig = px.histogram(df, x=x_col, title=f"Histogram of {x_col}")

            # Display the plot
            st.plotly_chart(fig)

        except Exception as e:
            st.error(f"Error reading or processing file: {e}")

if __name__ == "__main__":
    main()