import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn
st.title("Laptop Price Predictor : To predict the price of Laptop")
dataset=pickle.load(open("dataset_Laptop.pkl","rb"))
pipe=pickle.load(open("pipe_Laptop.pkl","rb"))

# creating various variables for input and output

Company=st.selectbox("Company Name",dataset["Company"].unique())
Type=st.selectbox("Type of Laptop",dataset["TypeName"].unique())
Ram=st.selectbox("RAM in GB",dataset["Ram"].sort_values().unique())
GPU=st.selectbox("GPU Manufacturer",dataset["Gpu"].unique())
OS=st.selectbox("Opreating System",dataset["OpSys"].unique())