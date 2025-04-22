import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Sidebar for navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Visualizations", "Upload Dataset"])

@st.cache_data()
def load_data(default=True, uploaded_file=None):
    if default:
        return pd.read_csv('datasets/data.csv')
    else:
        return pd.read_csv(uploaded_file)

if menu == "Upload Dataset":
    st.title("Upload Your Dataset")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file:
        df = load_data(default=False, uploaded_file=uploaded_file)
        st.success("Dataset loaded successfully!")
        st.dataframe(df)
    else:
        st.info("Please upload a dataset to proceed.")
else:
    # Load default dataset with refresh option
    if st.sidebar.button("Refresh Data"):
        st.cache_data.clear()
    df = load_data()

    if menu == "Home":
        st.title('My Data Analysis App')
        st.markdown("### Welcome to the interactive Data Analysis application.")
        st.info("Use the navigation menu to explore more features.")
        st.dataframe(df)

    elif menu == "Visualizations":
        st.title("Data Visualization")
        st.markdown("### Explore your data with interactive visualizations.")

        # Job Titles Visualization
        st.subheader('Top 10 Job Titles')
        job_count = df['job_title'].value_counts().head(10)
        fig1 = px.bar(job_count, job_count.index, job_count.values, title='Top 10 Job Titles')
        st.plotly_chart(fig1, use_container_width=True)
        
        # Customizable Graphs
        st.subheader("Custom Graphs")
        categories = df.select_dtypes(exclude=np.number).columns.tolist()
        st.success(f'Available categories: {", ".join(categories)}')
        
        selected_category = st.selectbox("Select a category", categories)
        graph_type = st.radio("Select graph type", ["Bar", "Pie", "Box", "Violin"])
        
        if graph_type == "Bar":
            counts = df[selected_category].value_counts()
            fig = px.bar(counts, counts.index, counts.values, title=f'Distribution of {selected_category}')
        elif graph_type == "Pie":
            counts = df[selected_category].value_counts()
            fig = px.pie(values=counts.values, names=counts.index, title=f'Distribution of {selected_category}')
        elif graph_type == "Box":
            fig = px.box(df, x=selected_category, y='salary_in_usd', title=f'Salary Distribution by {selected_category}')
        elif graph_type == "Violin":
            fig = px.violin(df, x=selected_category, y='salary_in_usd', title=f'Salary Distribution by {selected_category}')
        
        st.plotly_chart(fig, use_container_width=True)
