import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import random
import math
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

def linearregessionc19():
  data = pd.read_csv('https://github.com/arathi5056/datasets/blob/master/owid-covid-data.csv?raw=true')
  data = pd.DataFrame(data)
  #data.shape

  # Taking a backup of the data

  #data_bkp = data.copy()

  #data_bkp.shape

  # data_bkp.columns

  #data.index

  data.columns
  del data['continent'] # Dropping the Continent column as it has some blank values which can't be imputed
  del data['tests_units']

  #data.info()
  # data.set_index('iso_code',drop = True, inplace = True)
  #data.head()

  data.interpolate(limit_direction="both")
  data.fillna(0,inplace=True)
  #data.head(25)

  data.isna().any()

  covid_data = data.copy()

  # Split into train and test set
  # The split is an 80/20 Train/Test split

  np.random.seed(42) # Set a random seed for reproducability

  index = round(0.8 * len(data)) # An index to randomly subset data by rows

  train = covid_data[index:] 
  # train = data.sample(frac= 0.8,replace = True,random_state=123)
  train.shape
  # train.head(10)

  test = covid_data[-index:] # Creates a testing set with 20% of the full dataset chosen randomly
  #test.shape
  # test.head(10)

  # del train['tests_units']
  #train.info()

  from statsmodels.stats.outliers_influence import variance_inflation_factor

  X = train.loc[:,'total_cases':'excess_mortality_cumulative_per_million']
  # VIF dataframe
  vif_data = pd.DataFrame()
  vif_data["feature"] = X.columns
    
  # calculating VIF for each feature
  vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                            for i in range(len(X.columns))]
    
  #print(vif_data)
  #vif_data

  """For linear regression, it is absolutely essential that we deal with multi-collinearity between the variables. To detect multi-collinearity, we'll use the Variance Inflation Factor(VIF) to see how a particular variable is correlated with others.

  A VIF < 10 is the threshold to choose a variable for the final analysis.
  """

  temp = train.loc[:,['total_cases_per_million','new_cases_per_million','new_cases_smoothed_per_million','total_deaths_per_million','new_deaths_per_million',
              'new_deaths_smoothed_per_million','icu_patients_per_million','hosp_patients_per_million','weekly_icu_admissions','weekly_icu_admissions_per_million',
              'weekly_hosp_admissions_per_million','total_tests','total_tests_per_thousand','positive_rate','tests_per_case','total_boosters_per_hundred',
              'new_vaccinations_smoothed_per_million','new_people_vaccinated_smoothed_per_hundred','population','population_density','gdp_per_capita',
              'extreme_poverty','diabetes_prevalence','female_smokers','male_smokers','handwashing_facilities','hospital_beds_per_thousand','excess_mortality_cumulative_absolute',
              'excess_mortality_cumulative','excess_mortality']]

  vif_temp = pd.DataFrame()
  vif_temp["feature"] = temp.columns
    
  # calculating VIF for each feature
  vif_temp["VIF"] = [variance_inflation_factor(temp.values, i)
                            for i in range(len(temp.columns))]
    
  #print(vif_data)
  #vif_temp

  """The above shortlisted variables are the one's with the least VIF and hence, will be used to build the parsimonious model."""

  #temp_df = vif_temp[vif_temp['feature'] != ('excess_mortality_cumulative_absolute') or vif_temp['feature'] != ('excess_mortality_cumulative') or vif_temp['feature'] != ('excess_mortality')]
  # temp_df = vif_temp.iloc[0:27 :,]
  # temp_df

  list_x = vif_temp['feature']
  #list_x

  # length = len(train)
  x = train[list_x]
  x = sm.add_constant(x)
  #y = train[['life_expectancy','weekly_hosp_admissions']]
  y = train['excess_mortality_cumulative_per_million']

  # x = x.values.reshape(length, 4)
  # y = y.values.reshape(length, 4)

  model = sm.OLS(y,x)
  results = model.fit()
  data=results.summary()
  #print(results.summary())

  """After running the regression, we see that we do have a decent R^2 value of 68.8% which is not bad for an everchanging dataset. However, we see that Auto-correlation, another facet of multi-collinearity, is affecting our predictions and hence we can conclude that Linear Regression analysis is not the best option to analyse this data and deduce causality.

  ATime-Series analysis is more suited for this dataset.
  """

  # model_temp = make_pipeline(StandardScaler(with_mean = False),LinearRegression())
  #model_temp = LinearRegression()
  #model_temp.fit(x,y)
  #coef = model_temp.coef_
  #intercept = model_temp.intercept_
  #print('coef= ', coef)
  #print('intercept= ', intercept)
  #data=data+coef+intercept

  return data
