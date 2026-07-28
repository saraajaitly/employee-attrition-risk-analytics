from pathlib import Path
import streamlit as st
import joblib
import pandas as pd
MODEL_PATH = Path("models/gradient_boosting_model.pkl")
FEATURES_PATH = Path("models/feature_columns.pkl")


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


@st.cache_resource
def load_feature_columns():
    return joblib.load(FEATURES_PATH)
def preprocess_data(df):
    df = df.copy()

    columns_to_drop = [
        "EmployeeCount",
        "EmployeeNumber",
        "Over18",
        "StandardHours"
    ]

    df = df.drop(columns=columns_to_drop, errors="ignore")

    categorical_cols = [
        "BusinessTravel",
        "Department",
        "EducationField",
        "Gender",
        "JobRole",
        "MaritalStatus",
        "OverTime"
    ]

    df = pd.get_dummies(
        df,
        columns=categorical_cols,
        drop_first=True,
        dtype=int
    )

    feature_columns = load_feature_columns()

    df = df.reindex(columns=feature_columns, fill_value=0)

    return df
def predict_attrition(df):
    model = load_model()

    processed_df = preprocess_data(df)

    predictions = model.predict(processed_df)
    probabilities = model.predict_proba(processed_df)[:, 1]

    results = df.copy()

    results["Prediction"] = predictions
    results["Attrition Risk (%)"] = (probabilities * 100).round(2)

    return results
def categorize_risk(probability):

    if probability < 30:
        return "Low"

    elif probability < 60:
        return "Medium"

    return "High"
def add_risk_category(df):

    results = df.copy()

    results["Risk Category"] = results["Attrition Risk (%)"].apply(categorize_risk)

    return results
