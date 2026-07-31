import streamlit as st
import pandas as pd

from predictor import predict_attrition, add_risk_category


st.set_page_config(
    page_title="Predictions",
    page_icon="🔮",
    layout="wide"
)

st.title("Employee Attrition Prediction")

st.markdown(
    """
Upload an employee dataset to predict attrition risk using the trained Gradient Boosting model.
"""
)
st.subheader("📂 Upload Employee Dataset")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"],
    label_visibility="collapsed"
)

st.caption(
    "🛈 **Future enhancement:** Support custom HR datasets through "
    "automatic schema validation and intelligent column mapping."
)

st.markdown(
    "<h4 style='text-align:center;'>──────────── OR ────────────</h4>",
    unsafe_allow_html=True
)

load_sample = st.button(
    "✨ Load Sample Dataset",
    use_container_width=True
)
df = st.session_state.get("df")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state["df"] = df

elif load_sample:
    df = pd.read_csv(
        "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
    )
    st.session_state["df"] = df

if uploaded_file is not None or load_sample:
    

    if uploaded_file is not None:
        st.success("✅ Dataset uploaded successfully!")
    elif load_sample:
        st.success("✅ Sample dataset loaded successfully!")


    
    col1, col2 = st.columns(2)

    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))

    

    st.divider()
predict = st.button(
    "Predict Attrition",
    use_container_width=True,
    type="primary"
)

if predict:
    with st.spinner("Running prediction model..."):
        results = predict_attrition(df)
        results = add_risk_category(results)
        st.session_state["results"] = results
        
    st.success("✅ Predictions generated successfully!")

    st.subheader("Prediction Summary")

    high = (results["Risk Category"] == "High").sum()
    medium = (results["Risk Category"] == "Medium").sum()
    low = (results["Risk Category"] == "Low").sum()

    col1, col2, col3 = st.columns(3)

    col1.metric("🔴 High Risk", high)
    col2.metric("🟡 Medium Risk", medium)
    col3.metric("🟢 Low Risk", low)
    st.subheader("📋 Prediction Results")
    results_display = results.copy()

    results_display.rename(
        columns={"EmployeeNumber": "Employee ID"},
        inplace=True
    )

    
    display_cols = [
    "Employee ID",
    "JobRole",
    "Department",
    "Attrition Risk (%)",
    "Risk Category",
    "MonthlyIncome",
    "OverTime",
    "WorkLifeBalance"
]

    st.dataframe(
    results_display[display_cols],
    use_container_width=True,
    hide_index=True
)
    high_risk = results[results["Risk Category"] == "High"]
    download_df = high_risk[
    [
        "EmployeeNumber",
        "Department",
        "JobRole",
        "MonthlyIncome",
        "OverTime",
        "WorkLifeBalance",
        "Attrition Risk (%)",
        "Risk Category",
    ]
].copy()
    download_df.rename(
    columns={
        "EmployeeNumber": "Employee ID",
        "JobRole": "Job Role",
        "MonthlyIncome": "Monthly Income",
        "OverTime": "Overtime",
        "WorkLifeBalance": "Work-Life Balance",
    },
    inplace=True,
)
    csv = download_df.to_csv(index=False).encode("utf-8")
    st.info(
        f"🚨 {len(high_risk)} employees were identified as High Risk and can be exported for further HR review."
    )
    st.download_button(
        "Download High-Risk Employees",
        data=csv,
        file_name="high_risk_employees.csv",
        mime="text/csv",
        use_container_width=True,
    )
