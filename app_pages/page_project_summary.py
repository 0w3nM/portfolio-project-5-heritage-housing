import streamlit as st


def page_summary_body():

    st.write("* Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Dataset**\n"
        f"The dataset is representing a list of **houses**, in Ames, Iowa"
        f"focusing on their attributes. Floor Area, Basement, Garage,
        f"Kitchen, Lot, Porch, Wood Deck and Year Built,"
        f"with houses sale price between the years 1872 & 2010.")

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/).")

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering and having a visualisation of the"
        f" houses sale price and how it is correlated to the houses attributes.\n"
        f"* 2 - The client is interested in predicting the sale prices, "
        f"for the four houses that she has inherited."
    )
