import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_data, load_pkl_file
from src.machine_learning.evaluate import regression_performance, regression_evaluation, regression_evaluation_plots


def page_project_ml_model_body():

    version = 'v1'
    price_predict_pipe = load_pkl_file(
        f"outputs/ml_pipeline/price_predict/{version}/regressor_pipeline.pkl")
    feat_importance = plt.imread(
        f"outputs/ml_pipeline/price_predict/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/price_predict/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/price_predict/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/price_predict/{version}/y_train.csv")
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/price_predict/{version}/y_test.csv")

    st.write("---")

    st.write("**ML Model**: Sale Price Performance")

    st.write("---")

    st.success(
        f"* A regressor model was created to predict how houses in Ames, Iowa sold, as per the second business requirement.\n"
        f"* It was required by the client that a R2 score of at least **0.75** was needed.\n"
        f"* The score was passed by a score above **0.8** on both the train and test set.\n"
        f"* It would then show that the model is suitable at achieving the client's requests.\n"
        )

    st.write("---")

    st.write(f"Below are both the Pipeline steps and the best feature")

    st.write("---")

    # Pipeline Steps
    st.write("---")

    st.write("* Steps in the ML Pipeline")
    st.write(price_predict_pipe)

    st.write("---")

    # Best features
    st.write("---")

    st.write("* Importantly trained features")
    st.write(X_train.columns.to_list())

    st.write("---")

    # Train and Test sets Performance
    st.write("---")

    st.write("* Pipeline Performance")
    regression_performance(X_train, y_train, X_test, y_test, price_predict_pipe)

    regression_evaluation_plots(X_train, y_train, X_test, y_test, price_predict_pipe)
