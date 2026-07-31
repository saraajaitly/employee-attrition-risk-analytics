import streamlit as st

st.title("📘 About Employee Attrition Risk Analytics")

st.markdown("""
An end-to-end **Machine Learning web application** that predicts employee attrition risk,
explains predictions using **SHAP Explainability**, and provides personalized recommendations
to support **data-driven HR decision-making**.
""")

st.divider()

col1, col2, col3, col4 = st.columns([1.8,0.75,1.4,1])

with col1:
    st.metric("🤖 Model", "Gradient Boosting")

with col2:
    st.metric("🔍 Explainability", "SHAP")

with col3:
    st.metric("📄 Reports", "DOCX & CSV")

with col4:
    st.metric("🌐 Platform", "Streamlit")
st.divider()

st.header("🚀 Project Overview")

st.info("""
Employee Attrition Risk Analytics is an end-to-end Machine Learning web application designed to help organizations proactively identify employees who may be at risk of leaving.

The application analyzes employee workplace and demographic information to estimate attrition risk using a Gradient Boosting model. In addition to predictions, it provides SHAP-based explanations, personalized retention recommendations, interactive dashboards, and downloadable reports to support data-driven HR decision-making.
""")

st.divider()

st.header("Problem Statement")

st.write("""
Employee attrition is a major challenge for organizations, leading to increased recruitment costs, loss of experienced talent, reduced productivity, and disruptions to business operations.

In many cases, employees at risk of leaving are identified only after they resign, limiting the organization's ability to take timely action. Early identification of attrition risk enables HR teams to implement targeted retention strategies and improve workforce stability.

This application leverages Machine Learning to identify employees who may be at risk of attrition, providing interpretable predictions and actionable insights that support proactive HR decision-making.
""")

st.divider()

st.header("📊 Dataset")

left, right = st.columns(2)

with left:
    st.subheader("Dataset")

    st.markdown("""
**IBM HR Analytics Employee Attrition Dataset**

- 📄 Records: **1,470**
- 📊 Features: **35**
- 🎯 Target: **Attrition**
- 🏢 Domain: **Human Resources**
""")

with right:
    st.subheader("Key Features")
    st.markdown("""
- 👤 Age
- 🏢 Department
- 💼 Job Role
- 💰 Monthly Income
- ⏰ OverTime
- 😊 Job Satisfaction
- ⚖️ Work-Life Balance
- 🌱 Environment Satisfaction
- 📅 Years at Company
- 📈 Years Since Last Promotion
""")

st.success("**Target Variable:** Attrition (Yes / No)")

st.divider()

st.header("🤖 Machine Learning Pipeline")

st.write("""
The application follows a complete end-to-end machine learning workflow, transforming employee data into explainable predictions and actionable insights for HR professionals.
""")

st.markdown("""
###  Workflow

 **Employee Dataset**
➡️  **Data Preprocessing**
➡️  **Gradient Boosting**
➡️  **Risk Prediction**
➡️  **Risk Categorization**
➡️  **SHAP Explainability**
➡️  **Recommendations**
➡️  **CSV & DOCX Reports**
""")

st.subheader("Core Modules")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
**📈 Prediction**

Predict employee attrition risk from uploaded datasets.
""")

with col2:
    st.info("""
**📊 Dashboard**

Visualize attrition trends, KPIs, and risk distribution.
""")

with col3:
    st.info("""
**👤 Employee Insights**

View SHAP explanations, personalized recommendations, and downloadable reports.
""")

st.divider()

st.header("📈 Model Performance")

st.write("""
The application uses a **Gradient Boosting Classifier** trained on the IBM HR Analytics Employee Attrition dataset. The model was selected based on its ability to effectively capture complex relationships between employee characteristics and attrition risk while maintaining balanced predictive performance.
""")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Accuracy", "85.03%")

with col2:
    st.metric("Precision", "54.29%")

with col3:
    st.metric("Recall", "40.43%")

with col4:
    st.metric("F1 Score", "46.34%")

with col5:
    st.metric("ROC-AUC", "0.766")
st.caption(
    "The model was evaluated using Accuracy, Precision, Recall, F1 Score, and ROC-AUC to ensure reliable and balanced performance for employee attrition prediction."
)
st.success("""
**Why Gradient Boosting?**

Gradient Boosting delivered the best overall balance between predictive performance and generalization on the employee attrition dataset. It effectively captured complex relationships between employee attributes while providing reliable probability estimates that support risk categorization and SHAP-based explainability.
""")

st.divider()

st.header("🔍 SHAP Explainability")

st.write("""
Traditional machine learning models often provide predictions without explaining the reasoning behind them. To improve transparency and support informed HR decision-making, this application integrates **SHAP (SHapley Additive exPlanations)**.

For each employee, SHAP identifies the features that have the greatest influence on the predicted attrition risk, enabling users to understand *why* an employee has been classified as Low, Medium, or High Risk.
""")

st.subheader("Key Influential Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
- ⏰ OverTime
- ⚖️ Work-Life Balance
- 😊 Job Satisfaction
""")

with col2:
    st.markdown("""
- 🌱 Environment Satisfaction
- 💰 Monthly Income
- 📈 Years Since Last Promotion
""")

with col3:
    st.markdown("""
- 👔 Job Involvement
- 🏢 Business Travel
- 📍 Distance From Home
""")

st.success("""
**Why SHAP?**

Rather than acting as a black-box prediction model, the application provides transparent, interpretable insights that help HR professionals understand the factors contributing to attrition risk and make more informed retention decisions.
""")
st.caption(
    "Individual SHAP explanations are available in the Employee Insights page, where each prediction is accompanied by feature-level contributions and personalized recommendations."
)

st.divider()

st.header("🛠 Technology Stack")

left, right = st.columns(2)

with left:
    st.subheader("🤖 Machine Learning")

    st.markdown("""
- **Python** – Core programming language
- **Pandas & NumPy** – Data preprocessing and analysis
- **Scikit-learn** – Gradient Boosting model
- **SHAP** – Model explainability
""")

with right:
    st.subheader("💻 Application Development")

    st.markdown("""
- **Streamlit** – Interactive web application
- **Plotly & Matplotlib** – Data visualization
- **python-docx** – Employee report generation
- **Git & GitHub** – Version control
""")

st.subheader("Application Pages")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
### 📈 Prediction

- Upload employee dataset
- Predict attrition risk
- Export high-risk employees
""")

with col2:
    st.info("""
### 📊 Dashboard

- Organizational KPIs
- Risk distribution
- Department insights
""")

with col3:
    st.warning("""
### 👤 Employee Insights

- SHAP explanations
- Personalized recommendations
- Download employee report
""")
st.divider()

st.header("🚀 Future Scope")

st.write("""
The current application provides a complete end-to-end solution for employee attrition prediction and analysis. Future enhancements can further improve its scalability, usability, and real-world adoption.
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
### 📈 Analytics & Intelligence

- Real-time HR database integration
- Support for additional ML models
- Advanced workforce analytics
- Trend analysis over time
""")

with col2:
    st.markdown("""
### 💼 Enterprise Features

- User authentication & role-based access
- Email alerts for high-risk employees
- Cloud deployment & scalability
- Interactive executive dashboards
""")

st.success("""
The application is designed with a modular architecture, making it easy to extend with additional machine learning models, enterprise integrations, and advanced HR analytics in future versions.
""")
st.divider()

st.caption(
    "© 2026 Employee Attrition Risk Analytics • Built with Streamlit, Scikit-learn and SHAP for explainable HR decision support."
)