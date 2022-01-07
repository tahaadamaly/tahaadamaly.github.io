import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from  scipy import stats
from scipy.stats import linregress


# Setting up dataframes with stock data and cleaning dataframes
# Data downloaded from jbs.lk (requires login)
expo = pd.read_csv('data/PriceData_EXPO_3Y.csv')
expo = expo.drop(columns=['EX', 'PrevClose', 'Cha', 'Open', 'High', 'Low', 'Avg', 'Volume', 'Turnover', 'Trns', 'RSI', 'Return', 'DilutedPrice'])
expo = expo.rename(columns={'Date': 'date', 'Security': 'name', 'Close': 'price'})
for i in expo['name']:
    expo['name'] = 'EXPO'

aspi = pd.read_csv('data/IndexData_ASPI_3Y.csv')
aspi = aspi.drop(columns=['Turnover', 'Volume', 'Trades', 'Chg', 'Chg.1', 'ForeignBuy', 'ForeignSell', 'BS', 'ForeignNet', 'MarketCap', 'PER', 'RSI'])
aspi = aspi.rename(columns={'Date': 'date', 'Sector': 'name', 'Index': 'price'})

stock_data = pd.DataFrame()

stock_data['date'] = expo['date']
stock_data['expo'] = expo['price']
stock_data['aspi'] = aspi['price']

y = stock_data['expo']
x = stock_data['aspi']

# Polynomial model with 3 features
poly_model = make_pipeline(PolynomialFeatures(1), LinearRegression())
poly_model.fit(x[:, np.newaxis], y)
xfit = np.linspace(min(x), max(x), 2)
yfit = poly_model.predict(xfit[:, np.newaxis])

# Plotting data
plt.scatter(x, y)
plt.plot(xfit, yfit,color='crimson')
plt.xlabel('ASPI (Index)')
plt.ylabel('EXPO (LKR)')

# Additional statistics
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
r_squared="{:.2f}".format(r_value**2)

# Formatting
plt.legend(('Best fit', 'R-squared={}'.format(r_squared)), fontsize=15, loc="upper left", borderpad=0.4, edgecolor="black")
plt.title("CSE - Looking at the relationship between ASPI and EXPO", fontweight="bold")

print(slope, intercept, r_value, p_value, std_err)
print(r_squared)

plt.show()