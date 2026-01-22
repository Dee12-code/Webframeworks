import streamlit as st
import pandas as pd 
import numpy as np

#Random Functions
def make_predictions(df, model_choice):
    pass
def create_plot(predictions):
    pass

# 1. Page config (must be the first...)
st.set_page_config(
    page_title="ML App", layout = "wide")
 # 2. Title
st.title("Model Prediction")   
st.title("My First ML App")
st.write("Upload data and get predictions!")

# Have a sidebar for the input
with st.sidebar:
    Uploaded_file = st.file_uploader("Upload a file", type =["csv"])
    model_choice = st.selectbox("Model", ["Random Forest", "XGBoost"])

# Main content
if Uploaded_file:
    df = pd.read_csv(uploaded_file)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Input Data")
        st.dataframe(df.head())

    with col2:
        st.subheader("Predictions")
        predictions = make_predictions(df, model_choice)
        st.dataframe(predictions)
    
    # Visualization
    st.subheader("Results")
    fig = create_plot(predictions)
    st.plotly_chart(fig, use_container_width=True)




from sklearn import datasets
iris = datasets.load_iris()
