import streamlit as st

st.set_page_config(
    page_title="Employee Attrition Risk Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    padding-left:4rem;
    padding-right:4rem;
}

h1{
    color:#1F3A5F;
    font-weight:700;
}

h3{
    color:#374151;
}

</style>
""", unsafe_allow_html=True)
st.title("Employee Attrition Risk Analytics")

st.markdown("""
### Predict. Explain. Prevent.

Employee Attrition Risk Analytics is a machine learning application that
helps HR teams identify employees at risk of attrition, understand the
key factors driving that risk, and support proactive retention decisions.
""")

st.divider()


st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.caption("MODEL")
        st.markdown("### Gradient Boosting")
        st.write(
            "Selected as the production model after evaluating multiple baseline and tuned machine learning models."
        )

with col2:
    with st.container(border=True):
        st.caption("DATASET")
        st.markdown("### IBM HR Analytics")
        st.write(
            "Industry-standard HR analytics dataset containing employee demographics, workplace and job-related attributes."
        )

with col3:
    with st.container(border=True):
        st.caption("EXPLAINABILITY")
        st.markdown("### SHAP")
        st.write(
            "Provides transparent feature-level explanations that help HR teams understand the factors influencing each prediction."
        )

st.write("")

with st.container(border=True):

    st.markdown("### Who is this application for?")

    st.write(
        """
        Employee Attrition Risk Analytics is designed for **HR Managers, People Analytics Teams,
        HR Business Partners and organisational decision-makers** who need to identify employees
        at risk of attrition, understand the factors contributing to employee turnover and
        support proactive, data-driven retention strategies.
        """
    )