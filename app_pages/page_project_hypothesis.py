import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis")

    st.write("---")

    st.info(
        f"The project was crated to see what correlations there were between,
        f" the houses features and the sale price."
    )

    st.write("---")

    st.success(
        f"* It is shown in the study that there are 2 variables that have a strong correlation,"
        f" with the sale price **Overall Quality** and **Ground Living Area**."/n
        f"* Here it shows that houses with larger living facilities and/or have "
        f"a higher overall quality, affect the price of the house. "
    )
