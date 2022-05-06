import matplotlib.pyplot as plt
from io import StringIO
import numpy as np
def return_graphs():

    x = np.arange(0,np.pi*3,.1)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    #print(data)
    return data


import matplotlib.pyplot as plt
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


 

def return_graph_Totalcases():
  print('starte')
  covid_data =pd.read_csv('https://github.com/arathi5056/datasets/blob/master/owid-covid-data.csv?raw=true')
  del covid_data['continent']
  date_rearranged_df = covid_data.sort_values(['date'],ascending= True)
  latest_date = date_rearranged_df['date'].iat[-1]
  discard = ["OWID_"]
  
  # drop rows that contain the partial string "Sci"
  covid_data=covid_data[~covid_data.iso_code.str.contains('|'.join(discard))]
  

  print('starte2')

  total_df = covid_data[['iso_code','location','date','total_cases','total_deaths']]
  total_cases_df = total_df[total_df.date == latest_date].sort_values(['total_cases'],ascending=False)[1:11]
  total_deaths_df = total_df[total_df.date == latest_date].sort_values(['total_deaths'],ascending=False)[1:11]
  print(total_df['total_cases'])
  print('starte3')

  _x = total_cases_df.iso_code
  _y = total_cases_df.total_cases

  print(_x)
  print(_y)
  plt.figure(figsize=(14,10), dpi = 441)
  plt.bar(range(len(_x)),_y,width = 0.4)
 
  #for xx, yy in zip(range(len(_x)),_y):
  #    plt.text(xx, yy+5, str(yy), ha='center')
  print('starte4')
  plt.xticks(range(len(_x)),_x)
  plt.xlabel("Country")
  plt.ylabel("Total Cases")
  plt.title('Top countries of total cases')
  plt.plot()
  #plt.show()

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
  return graph


def return_graph_Totaldeaths():
  print('starte')
  covid_data =pd.read_csv('https://github.com/arathi5056/datasets/blob/master/owid-covid-data.csv?raw=true')
  del covid_data['continent']
  date_rearranged_df = covid_data.sort_values(['date'],ascending= True)
  latest_date = date_rearranged_df['date'].iat[-1]
  discard = ["OWID_"]
  
  # drop rows that contain the partial string "Sci"
  covid_data=covid_data[~covid_data.iso_code.str.contains('|'.join(discard))]
  

  print('starte2')

  total_df = covid_data[['iso_code','location','date','total_cases','total_deaths']]
  total_cases_df = total_df[total_df.date == latest_date].sort_values(['total_cases'],ascending=False)[1:11]
  total_deaths_df = total_df[total_df.date == latest_date].sort_values(['total_deaths'],ascending=False)[1:11]
  #print(total_df['total_cases'])
  print('starte3')

  

  _x = total_deaths_df.iso_code
  _y = total_deaths_df.total_deaths

  plt.figure(figsize=(14,10), dpi = 441)
  plt.bar(range(len(_x)),_y,width = 0.5)

  for xx, yy in zip(range(len(_x)),_y):
    plt.text(xx, yy+5, str(yy), ha='center')


  plt.xticks(range(len(_x)),_x)
  plt.xlabel("Country")
  plt.ylabel("Total Deaths")
  plt.title('Top countries of total deaths')
  plt.plot()

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
  return graph

def return_grid_IND():
  print('starte')
  covid_data =pd.read_csv('https://github.com/arathi5056/datasets/blob/master/owid-covid-data.csv?raw=true')
  del covid_data['continent']
  date_rearranged_df = covid_data.sort_values(['date'],ascending= True)
  latest_date = date_rearranged_df['date'].iat[-1]
  discard = ["OWID_"]
  
  # drop rows that contain the partial string "Sci"
  covid_data=covid_data[~covid_data.iso_code.str.contains('|'.join(discard))]
  

  print('starte2')

  total_df = covid_data[['iso_code','location','date','total_cases','total_deaths']]
  total_cases_df = total_df[total_df.date == latest_date].sort_values(['total_cases'],ascending=False)[1:11]
  total_deaths_df = total_df[total_df.date == latest_date].sort_values(['total_deaths'],ascending=False)[1:11]
  #print(total_df['total_cases'])
  print('starte3')
  IND_new_cases_df = covid_data[covid_data.iso_code == 'IND'][['date','new_cases']].fillna(0)
  IND_new_cases_df['date'] = IND_new_cases_df['date'].apply(lambda x:x[-5:])
  IND_new_cases_df
  _x = IND_new_cases_df.date
  _y = IND_new_cases_df.new_cases

  plt.figure(figsize = (20,8),dpi = 441)

  plt.plot(range(len(_x)),_y)
  plt.xticks(range(len(_x))[::15],_x[::15],rotation = 45)
  plt.title('Covid cases INDIA')
  plt.grid()
  #plt.show()
  
  plt.plot()
  

 
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
  return graph


