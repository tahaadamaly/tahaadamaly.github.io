# Not used

import formula1 as f1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from scipy import stats

rd = pd.read_excel('data/R&D_Data.xlsx')

def get_constructor_points(year, constructorID):
    df = f1.constructor_standings(year)
    df = df[['position', 'points', 'constructorID']]
    df = df[df.constructorID == constructorID]
    return df[['position', 'points']].reset_index(drop=True)

def plot_corr(team_name):
    team = pd.DataFrame()
    team['year'] = [i for i in range(2012, 2021)]
    rd1 = rd[rd.Team == team_name].T.reset_index().drop([0 ,10]).reset_index(drop=True)
    rd1.columns = ['year', 'rd_exp']
    team['rd_exp'] = rd1['rd_exp']
    points = []
    for i in range (2012, 2021):
        df = get_constructor_points(i, team_name)
        points.append(int(df['points'].values))
    team['points'] = points
    x = team['rd_exp'].astype(int)
    y = team['points'].astype(int)
    poly_model = make_pipeline(PolynomialFeatures(1), LinearRegression())
    poly_model.fit(x[:, np.newaxis], y)
    xfit = np.linspace(min(x), max(x), 2)
    yfit = poly_model.predict(xfit[:, np.newaxis])
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    r_squared="{:.2f}".format(r_value**2)
    print(slope, intercept, r_value, p_value, std_err)
    print(r_squared)
    plt.legend(('Best fit', 'R-squared={}'.format(r_squared)), fontsize=15, loc="upper left", borderpad=0.4, edgecolor="black")
    plt.title("Correlation between R&D and point scoring for {}".format(team_name), fontweight="bold")
    # Plotting data
    plt.scatter(x, y)
    plt.plot(xfit, yfit,color='crimson')
    plt.xlabel('R&D')
    plt.ylabel('Points')
    plt.show()

plot_corr('red_bull')
