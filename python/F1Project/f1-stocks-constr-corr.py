# This is used to access the stock data for mercedes and williams, as well as the constructor standings each year and create an
# CSV file that can be used in a vega chart
# Chart 5a and 5b

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.pytables import WORMTable
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from scipy import stats
from scipy.stats import linregress

# Access stock price data and separate into two different dataframes
stockprice = pd.read_csv('data/f1-mercedes-williams-stocks.csv')
mercedes_stock = stockprice[['year', 'mercedes']].rename(columns={'mercedes': 'price'}).reset_index(drop=True)
williams_stock = stockprice[['year', 'williams']].rename(columns={'williams': 'price'}).reset_index(drop=True)

# Access constructor standings data
constrstandings = pd.read_csv('data/f1_constr_points_yearly.csv')
constrstandings = constrstandings[constrstandings['constructorID'].isin(['williams', 'mercedes'])]
constrstandings = constrstandings[constrstandings['year'].isin([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])].reset_index()
constrstandings = constrstandings[['year', 'constructorID', 'points']]
mercedes_points = constrstandings[constrstandings.constructorID == 'mercedes'].reset_index(drop=True)
williams_points = constrstandings[constrstandings.constructorID == 'williams'].reset_index(drop=True)

mercedes_points_stocks = pd.DataFrame()
mercedes_points_stocks['year'] = mercedes_points['year']
mercedes_points_stocks['points'] = mercedes_points['points']
mercedes_points_stocks['stock'] = mercedes_stock['price']

williams_points_stocks = pd.DataFrame()
williams_points_stocks['year'] = williams_points['year']
williams_points_stocks['points'] = williams_points['points']
williams_points_stocks['stock'] = williams_stock['price']

mercedes_points_stocks.to_csv('data/mercedes-points-stockprice.csv')
williams_points_stocks.to_csv('data/williams-points-stockprice.csv')
