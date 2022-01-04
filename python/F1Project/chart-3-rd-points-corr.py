import collections
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from scipy import stats

# Obtaining constructor standings, data was obtained in chart-2-constructor-standings.py through Ergast F1 API
# This same data was presented in Section 2, however it is cleaned here and only years 2012-2020 are considered.
# See chart-2-constructor-standings.ipynb for method on data collection for constructor standings

constructor_standings = pd.read_csv('data/constructor-standings-2012-2021-proportions.csv')
constructor_standings = constructor_standings[['name', 'proptotalpoints', 'constructorID', 'year']]
constructor_standings.sort_values(by=['constructorID', 'year'], inplace=True)
constructor_standings.reset_index(drop=True, inplace=True)

# R&D Expenditure values here are the same as presented in section 1. See section 1 on webpage for full source list
rd_exp = pd.read_excel('data/R&D_Data.xlsx')
rd_exp.rename(columns={'team': 'constructorID'}, inplace=True)
rd_exp.sort_values(by=['constructorID', 'year'], inplace=True)
rd_exp.reset_index(drop=True, inplace=True)

# Combine data so that R&D expenditure and points scored can be compared
master = pd.DataFrame()
master['constructorID'] = constructor_standings['constructorID']
master['year'] = constructor_standings['year']
master['rd_exp'] = rd_exp['expenditure']
master['proptotalpoints'] = constructor_standings['proptotalpoints']

master.to_csv('data/f1-rd-constructor-standings.csv')
