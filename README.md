# Heratige Housing

> The project is a machine learning app to help a client predict the sale prices of houses in the Ames, Iowa.

## Deployment :

- Live Link:[Heratige Hosuing](https://pp5-heritage-house-25083f746480.herokuapp.com/)

## Business Requirements

- A client has inherited 4 houses in Ames, Iowa from her great-grandfather, and ask a Data Practitioner to help maximise the sale price.
- The client has a excellent understanding of prices in her home country of Belgium, and thinks her lack of knowledge of Iowan markets could affect the appraisals.

  1.The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.

  2.The client is interested in predicting the house sales price from her four inherited houses, and any other house in Ames, Iowa.

---

## CRISP-DM Workflow

The project followed particular steps and was developed using CRISP-DM(**Cross** **Industry** **Standard** **Process** for **Data Mining**)

- _Business Understanding_:
  This is a part where a conversation with the client takes place and discuss what is required for the project. This is would create the **Business Requirements**, as seen above.

- _Data Understanding_:
  Here is where the data is collected from the client and analysed to see if the data can answer the clients question. This is done through **Data Cleaning** as seen in the **Data Cleaning Notebook**.

- _Data Preparation_:
  This part makes sure that the data is cleaned and is the best it can be for the model, by carrying out **Feature Enginnering** task, that can be seen in the **Feature Enginnering Notebook**.

- _Modelling_:
  Here the data gets split into _train_ and _test_ sets to find the best model algorithm to use. The _train_ is used to valiate alogorithms that are then tweaked using hyperparameter. This is shown in the **Price Predict Notebook**.

- _Evaluation_:
  This part looks at the results of the _test_ set and chooses the best model performance that meets the requirements set. This is also shown in the \*_Price Predict Notebook_

- _Deployment_:
  The final part is creating a visualisation of the data collected for the client to see. Shown in the **Heroku** link at the top.

---

## Epics And User Stories

**Epic 1:** Information gathering and data collection

- **User Story** - As a user i need to be able to visualse the to verify its authenticity.

**Epic 2:** Data visualization, cleaning, and preparation

- **User Story** - As a user i need to view the data to the correlation between attribute of house and sale price.

**Epic 3:** Model training, optimization and validation

- **User Story** - As a user i need to be able to predict the sale price on the houses get their full worth and also any other house in the region.

**Epic 4:**Dashboard planning, designing, and development

- **User Story** - As a user i need to have a dashboard that is user friendly and display the information of the project, e.g. Summary, Hypothesis, Model Information, Attribute Correlations and Predicted Sale Price.

**Epic 5:** _Dashboard deployment and release_

- **User Story** - As a user i need the relevant information easily displayed through the dashboard so i can use it to predict prices.

---

## Hypothesis

- There was a hypothesis posed before starting the project.

**Hypothesis**: Houses that are of higher quality and larger in space, have a sales price that is higher than those that dont.
**Validation**: By studying the correlation between both the size of the houses and the overall quality variables, sales price variable as the target.

---

## ML Business Case

- The purpose of the project was to create an ML model that predicts the sale price of houses in Ames, Iowa.
- The ideal outcome is to create a dashboard for the client to view and input predictions on sale prices of the inherited homes for the maximum price.
- The model success metrics are:
  - On both train and test sets the R2 score must be atleast **0.75**.
  - The ML model is considered to have failed should the R2 number not rise above **0.75** on either of the train and test sets.
  - If the model predictions are off by **50%** for **30%** of the inputs in a years use, it is also considered a failure, and a new model should be deployed.
- The continuous value for the sale price is what will define the output. Both for the client's inherited properties and any house in Ames, Iowa, using infrmation of the house attributes.
- Heuristics: Currently, there is no approach to predict the sale price of houses.
- The dataset acquired from Kaggle was used as the training data. This dataset has a vast amount of house records (1.5 thousand) for the area.
  - SalePrice is the target variable, all other variables in the dataset being looked at to use in the model.

---

## Dashboard Design

**Page 1**: _Project Summary_

- Description of the Project.
- Dataset Information.
- Business Requirements.

**Page 2**: _Price Correlation Analysis_

- A sample of the data.
- Scatter & Histogram Plots showing important features.
- Conclusions of Spearman and Pearson Correlation plots.
- PPS (Power Predictive Score) Analysis.

**Page 3**: _Price Predictor_

- Property attributes input to predict sale price.
- Display the price that was predicted.
- Ability to use clients data to predict sale price of inherited houses.

**Page 4**: _Project Hypothesis_

- Detailing the hypothesis and why it is vaild.

**Page 5**: _ML Model Performance_

- Pipeline information for training the model .
- Features that are important for the model.
- Review of the performance.

---

# Dataset Content

Sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data)
The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

| Variable      | Meaning                                                                 | Units                                                                                                                                                                   |
| :------------ | :---------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1stFlrSF      | First Floor square feet                                                 | 334 - 4692                                                                                                                                                              |
| 2ndFlrSF      | Second-floor square feet                                                | 0 - 2065                                                                                                                                                                |
| BedroomAbvGr  | Bedrooms above grade (does NOT include basement bedrooms)               | 0 - 8                                                                                                                                                                   |
| BsmtExposure  | Refers to walkout or garden level walls                                 | Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement                                                                       |
| BsmtFinType1  | Rating of basement finished area                                        | GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement |
| BsmtFinSF1    | Type 1 finished square feet                                             | 0 - 5644                                                                                                                                                                |
| BsmtUnfSF     | Unfinished square feet of basement area                                 | 0 - 2336                                                                                                                                                                |
| TotalBsmtSF   | Total square feet of basement area                                      | 0 - 6110                                                                                                                                                                |
| GarageArea    | Size of garage in square feet                                           | 0 - 1418                                                                                                                                                                |
| GarageFinish  | Interior finish of the garage                                           | Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage                                                                                                    |
| GarageYrBlt   | Year garage was built                                                   | 1900 - 2010                                                                                                                                                             |
| GrLivArea     | Above grade (ground) living area square feet                            | 334 - 5642                                                                                                                                                              |
| KitchenQual   | Kitchen quality                                                         | Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor                                                                                                        |
| LotArea       | Lot size in square feet                                                 | 1300 - 215245                                                                                                                                                           |
| LotFrontage   | Linear feet of street connected to property                             | 21 - 313                                                                                                                                                                |
| MasVnrArea    | Masonry veneer area in square feet                                      | 0 - 1600                                                                                                                                                                |
| EnclosedPorch | Enclosed porch area in square feet                                      | 0 - 286                                                                                                                                                                 |
| OpenPorchSF   | Open porch area in square feet                                          | 0 - 547                                                                                                                                                                 |
| OverallCond   | Rates the overall condition of the house                                | 10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor                                 |
| OverallQual   | Rates the overall material and finish of the house                      | 10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor                                 |
| WoodDeckSF    | Wood deck area in square feet                                           | 0 - 736                                                                                                                                                                 |
| YearBuilt     | Original construction date                                              | 1872 - 2010                                                                                                                                                             |
| YearRemodAdd  | Remodel date (same as construction date if no remodelling or additions) | 1950 - 2010                                                                                                                                                             |
| SalePrice     | Sale Price                                                              | 34900 - 755000                                                                                                                                                          |

---

# Main Data Analysis and Machine Learning

_Below is a list of the libraires used:

- numpy==1.18.5
- pandas==1.4.2
- matplotlib==3.3.1
- seaborn==0.11.0
- ydata-profiling==4.4.0
- plotly==4.12.0
- ppscore==1.2.0
- streamlit==0.85.0
- feature-engine==1.0.2
- imbalanced-learn==0.8.0
- scikit-learn==0.24.2
- xgboost==1.2.1
- yellowbrick==1.3
- Jinja2==3.1.1
- MarkupSafe==2.0.1
- protobuf==3.20
- ipywidgets==8.0.2
- altair<5

---

## Development & Deployment

- [GitHub](https://github.com/) was used to house the repository,
- [Code Anywhere](https://codeanywhere.com/) was used to create the project.
- [Jupyter Notebooks](https://jupyter.org/) was used to manipluate the date into charts and pipelines.
- [Heroku](https://www.heroku.com/) used to deploy the project.
- [Kaggle](https://www.kaggle.com/) gave access the dataset
- [Streamlit](https://streamlit.io/) used for the development of the online app interface.

---

## Python Testing

All Python Files checked through [CI Python Linter](https://pep8ci.herokuapp.com/)

---

## Credits

- I used the Code Instiute Churnometer Walkthrough

* [CodeInstitute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DDA101+2021_T4/courseware/bba260bd5cc14e998b0d7e9b305d50ec/c83c55ea9f6c4e11969591e1b99c6c35/)
* [CodeInstitute](https://github.com/Code-Institute-Solutions/churnometer/blob/main/jupyter_notebooks/02%20-%20Churned%20Customer%20Study.ipynb/)

- Aswell as these previous students projects through Slack as guidance through out the making of this project:

* [Uriem](https://github.com/URiem/heritage-housing-PP5/blob/main/jupyter_notebooks/01_DataCollection.ipynb)
* [Knutinator](https://github.com/knutinator/heritage-housing/blob/main/jupyter_notebooks/01%20Data%20Collection.ipynb)
* [ChrisCherng](https://github.com/ChrisCherng/heritage-housing/blob/main/jupyter_notebooks/02.%20HousePriceCorrelation.ipynb/)

- When i needed more information of PPS & Pearson/Spearman Correlation and threshold I used:

* [CodeInstitute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DDA101+2021_T4/courseware/468437859a944f7d81a34234957d825b/c8ea2343476c48739676b7f03ba9b08e/)
* [CodeInstitute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DDA101+2021_T4/courseware/468437859a944f7d81a34234957d825b/c8ea2343476c48739676b7f03ba9b08e/?child=first/)
* [GitHub](https://github.com/8080labs/ppscore#api/)
* [Statistic Solutions](https://www.statisticssolutions.com/free-resources/directory-of-statistical-analyses/pearsons-correlation-coefficient/#:~:text=High%20degree%3A%20If%20the%20coefficient,to%20be%20a%20small%20correlation)

- When i was stuck on how to use Stremlit i went back to:

* [Streamlit](https://docs.streamlit.io/library/api-reference)

- To help with the Feature Engineering section i used:

* [CodeInstitute](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/1f851533cd6a4dcd8a280fd9f37ef4e2/bb0bf41fb8744b46813c0f52a74b9b11/)
* [CodeInstitute](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/1f851533cd6a4dcd8a280fd9f37ef4e2/bb0bf41fb8744b46813c0f52a74b9b11/)
