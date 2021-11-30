# Week 10 Lecture 

# Imports
import yfinance as yf
import pandas as pd
import json
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
import seaborn as sns
sns.set()
from scipy.stats import linregress
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from sklearn.linear_model import LinearRegression

"""
nvda = yf.Ticker("NVDA").history(period='5y')
tsla = yf.Ticker("TSLA").history(period='5y')
ryaay = yf.Ticker("RYAAY").history(period='5y')
wizz = yf.Ticker("WIZZ.L").history(period='5y')


dfs = []
for x in ['NVDA', 'TSLA', 'RYAAY', 'WIZZ.L']:
    df = yf.Ticker(x).history(period='5y')
    df = df[['Close']]
    df['Name'] = x
    dfs.append(df)


# Stacking dataframes on top of each other
pd.concat(dfs)


# Joining dataframes together (Date is the same but new name and close columns are needed, so rsuffix is added)
ryan = dfs[2]
wizz = dfs[3]
nvda = dfs[0]

ryan = ryan.join(wizz, rsuffix='_wizz').join(nvda, rsuffix='_nvda')


dfz = pd.DataFrame()
for x in dfs:
    stock_name = x['Name'].values[0]
    stock_name = stock_name.replace('.', '')
    x = x[['Close']]
    x.columns=[stock_name]
    dfz=x.join(dfz)

dfz.to_csv('data/my_stock.csv')
"""


############# Part two - Seaborn ###################

stocks=pd.read_csv('data/my_stock.csv')
stocks.head(2)

x = stocks['Date'].values
x = pd.to_datetime(x) #let's make this a proper date
y1 = stocks[stocks.columns[1]]
y2 = stocks[stocks.columns[2]]
y3 = stocks[stocks.columns[3]]
y4 = stocks[stocks.columns[4]]

# Plot the data with Matplotlib defaults
"""
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.legend(stocks.columns[1:], ncol=2, loc='upper left')
"""

"""
data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    plt.hist(data[col], alpha=0.5)

for x in stocks.columns[1:]:
    plt.hist(stocks[x], alpha=0.5)
"""

######### Normalisation #########
"""
wizz_max=stocks['WIZZL'].max()
wizz_min=stocks['WIZZL'].min()
wizz_range=wizz_max-wizz_min
#print(wizz_max,wizz_min,wizz_range)

stocks['WIZZL_minmax_norm']=(stocks['WIZZL']-wizz_min)/wizz_range

wizz_max=stocks['WIZZL_minmax_norm'].max()
wizz_min=stocks['WIZZL_minmax_norm'].min()
wizz_range=wizz_max-wizz_min
#print(wizz_max,wizz_min,wizz_range)

"""

"""

for x in stocks.columns[1:5]:
  x_max=stocks[x].max()
  x_min=stocks[x].min()
  x_range=x_max-x_min
  stocks[x+'_minmax_norm']=(stocks[x]-x_min)/x_range




for x in stocks.columns[-4:]:
    plt.hist(stocks[x], alpha=0.5,bins=20)
    plt.legend(stocks.columns[-4:])



stock_stack=stocks.set_index('Date').stack().reset_index()
stock_stack.columns=['Date','Stock','Value']
stock_stack['Date']=pd.to_datetime(stock_stack['Date'])
stock_stack=stock_stack[stock_stack['Stock'].str.contains('minmax_norm')]
#print(stock_stack.head())

sns.lineplot(x='Date', y='Value', hue='Stock', data=stock_stack,legend=False)
plt.legend(stock_stack['Stock'].unique(),loc=2)
"""


######### Z-score #########

for x in stocks.columns[1:5]:
  stocks[x+'_z_norm']= (stocks[x] - stocks[x].mean())/stocks[x].std()


stock_stack=stocks.set_index('Date').stack().reset_index()
stock_stack.columns=['Date','Stock','Value']
stock_stack['Date']=pd.to_datetime(stock_stack['Date'])
stock_stack=stock_stack[stock_stack['Stock'].str.contains('z_norm')]
#print(stock_stack.head())



"""
sns.lineplot(x='Date', y='Value', hue='Stock', data=stock_stack,legend=False)
plt.legend(stock_stack['Stock'].unique(),loc=2)
"""
"""
for x in stocks.columns[-4:]:
    plt.hist(stocks[x], alpha=0.5,bins=20)
    plt.legend(stocks.columns[-4:])
"""

"""
for x in stocks.columns[-4:]:
    sns.kdeplot(stocks[x])
"""

################### PAIR PLOTS ####################
iris = sns.load_dataset("iris")

#sns.pairplot(iris, hue='species', height=1.5)

"""
sns.lineplot(x='Date', y='Value', hue='Stock', 
             data=stock_stack,legend=False)
plt.legend(stock_stack['Stock'].unique(),loc=2)
"""

#sns.pairplot(stocks[stocks.columns[-4:]], height=2.5)




################### REGRESSION ####################


#sns.regplot(x='TSLA',y='NVDA',data=stocks)

slope, intercept, rvalue, pvalue, stderr = linregress(x=stocks.dropna()['TSLA'], y=stocks.dropna()['NVDA'])
print('y = ',np.round(slope,2),' * x + ',np.round(intercept,2))
print('R² = ',np.round(rvalue**2,2))
np.corrcoef(stocks.dropna()['TSLA'], stocks.dropna()['NVDA'])



################### LINEAR REGRESSION ####################


rng = np.random.RandomState(1)
x = 10 * rng.rand(50)
y = 2 * x - 5 + rng.randn(50)

model = LinearRegression(fit_intercept=True)

model.fit(x[:, np.newaxis], y)

xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])
"""
plt.scatter(x, y)
plt.plot(xfit, yfit)

plt.show()


print("Model slope:    ", model.coef_[0])
print("Model intercept:", model.intercept_)
"""


####### BASIS FUNCTION REGRESSION #######

from sklearn.preprocessing import PolynomialFeatures
x = np.array([2, 3, 4])
poly = PolynomialFeatures(3, include_bias=False)
poly.fit_transform(x[:, None])

from sklearn.pipeline import make_pipeline
poly_model = make_pipeline(PolynomialFeatures(7), LinearRegression())


rng = np.random.RandomState(1)
x = 10 * rng.rand(50)
y = np.sin(x) + 0.1 * rng.randn(50)

poly_model.fit(x[:, np.newaxis], y)
yfit = poly_model.predict(xfit[:, np.newaxis])

#plt.scatter(x, y)
#plt.plot(xfit, yfit)

stocks=pd.read_csv('data/my_stock.csv')

x = stocks.dropna()['TSLA']
y = stocks.dropna()['NVDA']

poly_model = make_pipeline(PolynomialFeatures(3),
                           LinearRegression())
poly_model.fit(x[:, np.newaxis], y)
xfit = np.linspace(min(x), max(x), 1000)
yfit = poly_model.predict(xfit[:, np.newaxis])

plt.scatter(x, y)
plt.plot(xfit, yfit,color='crimson')
plt.xlabel('TSLA')
plt.ylabel('NVDA')

plt.show()

