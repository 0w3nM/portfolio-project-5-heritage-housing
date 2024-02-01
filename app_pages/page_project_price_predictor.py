import streamlit as st
import numpy as np
import pandas as pd

# Load Files


def page_project_price_predictor_body():
    version = 'v1'
    df_inherited_houses_data = load_ingerited_houses_data()
    sale_pipeline = load_pkl_file(
        f"outputs/ml_pipeline/price_predict/{version}/regressor_pipeline.pkl")
    price_features = (pd.read_csv(f"outputs/ml_pipeline/price_predict/{version}/X_train.csv")
                        .columns
                        .to_list())

    df = pd.read_csv(
        "inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")

    st.write("* Sale Price Predictor On Inherited Houses")
    st.write("---")

    st.success(
        f"* The client wishes to predict what the possible sale price"
        f"  and value are for, four inherited properties in Ames, Iowa")

    st.write("---")

    st.info(
            f" Four features of the property will be the focus of the price prediction.\n"
            f" Selections can be made by the client on any of the four features.\n"
            f" The machine learning model identified the best features to predict Sale Price"
            f" as **OverallQual**, **GarageArea**, **2ndFlSF** and **TotalBsmtSF**")

    st.write("---")

    # Live Data Generator
    X_live=DrawInputWidgets()

    price_predict=predict_sale_price(X_live, price_features, sale_pipeline)

    if st.button("Predict Sale Price"):
        st.success(f"Predicted house price: {predict_sale_price}")

    st.write("---")

# Widets Creation Function
def DrawInputsWidgets():

    # Load Dataset
    df=load_house_prices_data()
    percentageMin, percentageMax=0.4, 2.0

    # Widgets for the 4 features
    col01, col02=st.beta_columns(2)
    col03, col04=st.beta_columns(2)

    # Empty DataFrame for the live Data
    X_live=pd.DataFrame([], index=[0])

    # Widget based on value, and set initial value
    with col01:
        feature="OverallQual"
        st_widget=st.number_input(
            label='Overall Quality',
            min_value=1,
            max_value=10,
            value=int(df[feature].median()),
            step=1
        )
    X_live[feature]=st_widget

    with col02:
        feature="GarageArea"
        st_widget=st.number_input(
            label="Garage Area SQFT",
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            step=20
        )
        X_live[feature]=st_widget

    with col03:
        feature="2ndFlrSF"
        st_widget=st.number_input(
            label='2nd Floor SQFT',
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            step=20
        )
    X_live[feature]=st_widget

    with col04:
        feature="TotalBsmtSF"
        st_widget=st.number_input(
            label='Total Basement SQFT',
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            step=20
        )
    X_live[feature]=st_widget


    return X_live
