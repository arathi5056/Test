#import matplotlib.pyplot as plt
from io import StringIO

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
from io import BytesIO
import uuid, base64

def get_corelation(x, y):
  print(x + " " + y)
  #data = pd.read_csv("Test/update2q1-15.csv") 
  data =pd.read_csv('https://github.com/arathi5056/datasets/blob/master/owid-covid-data.csv?raw=true')
  list1= data.columns.values
  #print(list1)
  x = data[x].corr(data[y]) 
  #print(data.corr())
  #print(x)
  return x


def plot_correlation(x, y):
  print('starte')
  covid_data =pd.read_csv('https://github.com/arathi5056/datasets/blob/master/owid-covid-data.csv?raw=true')
  del covid_data['continent']
  date_rearranged_df = covid_data.sort_values(['date'],ascending= True)
  latest_date = date_rearranged_df['date'].iat[-1]
  discard = ["OWID_"]
  
  # drop rows that contain the partial string "Sci"
  covid_data=covid_data[~covid_data.iso_code.str.contains('|'.join(discard))]
  

  print('starte2')
  #plt.figure(figsize = (20,8),dpi = 441)
  #covid_data[x].plot(kind ="hist")
  #covid_data[y].plot(kind ="hist")  
  
  plt.scatter(covid_data[x], covid_data[y])
  #plt.plot(range(len(x)),y)
  #plt.xticks(range(len(_x))[::15],_x[::15],rotation = 45)
  #plt.title('Covid cases INDIA')
  #plt.grid()
  #plt.show()
  
  plt.plot()
  plt.show()

 
  #imgdata = StringIO()
  #fig = plt.figure()
  #fig.savefig(imgdata, format='svg')
  #imgdata.seek(0)
  #data = imgdata.getvalue()
  #print(data)
  
  buffer = BytesIO()
  plt.savefig(buffer, format='png')
  buffer.seek(0)
  image_png = buffer.getvalue()
  graph = base64.b64encode(image_png)
  graph = graph.decode('utf-8')
  buffer.close()
 
  plt.tight_layout()
  print('starte done')
  return graph