# Import library
import streamlit as st


# Run prediction from pipeline
def predict_price(X_live, property_features, sale_price_pipeline):

    # from live data, subset features related to this pipeline
    X_price_live = X_live.filter(features)

    # predict
    sale_prediction = int(pipeline.predict(X_price_live))

    return sale_prediction
