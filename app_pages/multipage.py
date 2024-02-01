import streamlit as st

# load pages scripts
from app_pages.page_project_summary import page_project_summary_body
from app_pages.page_sale_price_correlation_analysis import page_sale_price_correlation_analysis_body
from app_pages.page_project_price_predictor import page_project_price_predictor_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_project_ml_model import page_project_ml_model_body

app = MultiPage(app_name="Heritage Housing Predictor")

# Add your app pages here using .add_page()
app.add_page("Project Summary", page_project_summary_body)
app.add_page("Price Correlation Analysis", page_sale_price_correlation_analysis_body)
app.add_page("Price Predictor", page_project_price_predictor_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML: Model", page_project_ml_model_body)

app.run()