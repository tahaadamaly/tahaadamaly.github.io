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
#mercedes_points_stocks.to_csv('data/mercedes-points-stockprice.csv')
williams_points_stocks = pd.DataFrame()
williams_points_stocks['year'] = williams_points['year']
williams_points_stocks['points'] = williams_points['points']
williams_points_stocks['stock'] = williams_stock['price']
#williams_points_stocks.to_csv('data/williams-points-stockprice.csv')

""" 
# Regressions for mercedes

x = mercedes_stock['price']
y = mercedes_points['points']


# Polynomial model with 3 features
poly_model = make_pipeline(PolynomialFeatures(1), LinearRegression())
poly_model.fit(x[:, np.newaxis], y)
xfit = np.linspace(min(x), max(x), 2)
yfit = poly_model.predict(xfit[:, np.newaxis])

# Plotting data
plt.scatter(x, y)
plt.plot(xfit, yfit,color='crimson')
plt.xlabel('Stock Price')
plt.ylabel('Points Scored')

# Additional statistics
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
r_squared="{:.2f}".format(r_value**2)

# Formatting
plt.legend(('Best fit', 'R-squared={}'.format(r_squared)), fontsize=15, loc="upper left", borderpad=0.4, edgecolor="black")
plt.title("Formula 1 - The relationship between stock price and points scored", fontweight="bold")

print(slope, intercept, r_value, p_value, std_err)
print(r_squared)

plt.show()"""