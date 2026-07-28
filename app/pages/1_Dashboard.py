import streamlit as st
import pandas as pd

from predictor import predict_attrition, add_risk_category

st.set_page_config(
    page_title="Dashboard",
    layout="wide"
)

st.title("Dashboard")
df = pd.read_csv("data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv")

results = predict_attrition(df)
results = add_risk_category(results)

st.dataframe(results.head())