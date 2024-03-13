import plotly.express as px
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_management import load_house_data
sns.set_style("whitegrid")


def page_sale_price_correlation_analysis_body():

    # load data
    df = load_house_data()

    vars_to_study = ['OverallQual', 'GrLivArea', 'GarageArea',
                     'TotalBsmtSF', 'YearBuilt', '1stFlrSF']

    st.write("* House Sale Price Analysis")
    st.info(
        f"* The client is interested in how the houses attributes correlate "
        f"to the houses sale price. The client wishes to have a visualisation of "
        f"the data.")

    if st.checkbox("Inspect Price Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    st.write(
        f"* A study in the correlation was conducted in the notebook for a better, "
        f"understanding how the variables are correlated to the house sale price. \n"
        f"The study shows that the most correlated variable are: **{vars_to_study}**"
    )

    st.info(
        f"The plots below show the most correlated attributes associated with the sale price.\n"
        f"* Heatmaps\n"
        f"* Scatteplots\n"
        f"* The plots use *Spearman Correlation*, *Pearson Correlation* and *PPS(Predictive Power Score)*\n"
    )

    st.write("---")

    if st.checkbox("Spearman Correlation"):
        df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
        heat_corr(df=df_corr_spearman, threshold=0.5, figsize=(20, 12), font_annot=15)

    if st.checkbox("Person Correlation"):
        df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
        heat_corr(df=df_corr_spearman, threshold=0.5, figsize=(20, 12), font_annot=15)

    if st.checkbox("PPS"):
        df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
        heatmap_pps(df=pps_matrix, threshold=0.15, figsize=(20, 12), font_annot=15)


def sale_price_correlation_scatter(df, vars_to_study):
    target_var = 'SalePrice'
    fig, axes = plt.subplots(figsize=(10, 5))
    axes = sns.scatterplot(data=df, x=col, y=target_var)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)


def sale_price_correlation_histogram(df, vars_to_study):
    target_var = 'SalePrice'
    fig, axes = plt.subplots(figsize=(10, 5))
    axes = sns.histplot(data=df, x=col, y=target_var)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)


def plot_corr_heatmap(df, threshold, figsize=(20, 12), font_annot=8):
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True
        fig, axes = plt.subplots(figsize=figsize)
        sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                    mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=axes,
                    linewidth=0.5
                    )
        axes.set_yticklabels(df.columns, rotation=0)
        plt.ylim(len(df.columns), 0)
        plt.show()
        st.pyplot(fig)


def heatmap_pps(df, threshold, figsize=(20, 12), font_annot=8):
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[abs(df) < threshold] = True
        fig, ax = plt.subplots(figsize=figsize)
        ax = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True, mask=mask, cmap='rocket_r', annot_kws={"size": font_annot}, linewidth=0.05, linecolor='grey')
        plt.ylim(len(df.columns), 0)
        plt.show()
        st.pyplot(fig)


def calc_pps(df):
    pps_matirx_raw = pps.matrix(df)
    pps_matrix = pps_matirx_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')

    return df_corr_pearson, df_corr_spearman


def calc_corr(df):
    df_corr_pearson = df.corr(method="pearson")
    df_corr_spearman = df.corr(method="spearman")

    return pps_matrix
