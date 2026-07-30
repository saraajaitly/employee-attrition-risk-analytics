import streamlit as st
import pandas as pd
import plotly.express as px

from predictor import predict_attrition, add_risk_category


st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)


def load_dashboard_data():

    results = st.session_state.get("results")
    if results is None:
        st.warning("⚠️ Please upload a dataset and run predictions first.")
        st.stop()
    return results


results = load_dashboard_data()

st.title("Dashboard")
st.caption("Employee Attrition Risk Overview")
# -----------------------------
# KPI Metrics
# -----------------------------

total_employees = len(results)

high_risk = (results["Risk Category"] == "High").sum()
medium_risk = (results["Risk Category"] == "Medium").sum()
low_risk = (results["Risk Category"] == "Low").sum()

average_risk = results["Attrition Risk (%)"].mean()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Employees", f"{total_employees:,}")
col2.metric("High Risk", high_risk)
col3.metric("Medium Risk", medium_risk)
col4.metric("Low Risk", low_risk)
col5.metric("Average Risk", f"{average_risk:.1f}%")
st.divider()
left, right = st.columns(2)
with left:

    st.subheader("Risk Distribution")
    

    risk_counts = (
        results["Risk Category"]
        .value_counts()
        .reindex(["High", "Medium", "Low"])
        .reset_index()
    )

    risk_counts.columns = ["Risk Category", "Employees"]

    fig = px.bar(
        risk_counts,
        x="Risk Category",
        y="Employees",
        color="Risk Category",
        text="Employees",
        color_discrete_map={
            "High": "#d9534f",
            "Medium": "#f0ad4e",
            "Low": "#5cb85c",
        },
    )

    fig.update_layout(
        showlegend=False,
        height=360,
        margin=dict(l=20, r=20, t=20, b=20),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    fig.update_xaxes(title=None)

    fig.update_yaxes(title=None)

    fig.update_traces(
        textposition="outside",
        textfont_size=15
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("Department-wise Risk")

    dept_risk = (
        results.groupby("Department")["Attrition Risk (%)"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        dept_risk,
        x="Department",
        y="Attrition Risk (%)",
        text="Attrition Risk (%)",
        color_discrete_sequence=["#4F8EF7"]
    )

    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside"
    )

    fig.update_layout(
        showlegend=False,
        height=360,
        margin=dict(l=10, r=10, t=5, b=10),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    fig.update_xaxes(title=None)
    fig.update_yaxes(
        title=None,
        range=[15, 32]
    )

    st.plotly_chart(fig, use_container_width=True)    

st.markdown("<br>", unsafe_allow_html=True)

left, right = st.columns(2)
with left:

    st.subheader("Job Role Risk")

    role_risk = (
        results.groupby("JobRole")["Attrition Risk (%)"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig = px.bar(
        role_risk,
        x="JobRole",
        y="Attrition Risk (%)",
        text="Attrition Risk (%)",
        color_discrete_sequence=["#8B5CF6"]
    )

    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside"
    )

    fig.update_layout(
        showlegend=False,
        height=360,
        margin=dict(l=10, r=10, t=5, b=10),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    fig.update_xaxes(title=None)

    fig.update_yaxes(
        title=None
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )

with right:

    st.subheader("📌 Key Insights")

    highest_role = (
        results.groupby("JobRole")["Attrition Risk (%)"]
        .mean()
        .idxmax()
    )

    highest_role_risk = (
        results.groupby("JobRole")["Attrition Risk (%)"]
        .mean()
        .max()
    )

    highest_department = (
        results.groupby("Department")["Attrition Risk (%)"]
        .mean()
        .idxmax()
    )

    highest_department_risk = (
        results.groupby("Department")["Attrition Risk (%)"]
        .mean()
        .max()
    )

    st.info(
        f"""
### Executive Summary

• **{high_risk} employees** are classified as **High Risk**.

• **{highest_role}** has the highest predicted attrition risk (**{highest_role_risk:.1f}%**).

• **{highest_department}** has the highest average departmental risk (**{highest_department_risk:.1f}%**).

• The average predicted attrition risk across the workforce is **{average_risk:.1f}%**.

• Focus retention efforts on high-risk employees and departments to reduce potential turnover.
"""
    )
    