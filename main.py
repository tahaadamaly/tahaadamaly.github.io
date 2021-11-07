import formula1 as f1
from tabulate import tabulate
import pandas

def pprint_df(dframe):
    print(tabulate(dframe, headers='keys', tablefmt='psql', showindex=False))

def get_driver_pos(year, race_num, driver_number):
    df = f1.get_race_result(year, race_num)   
    pos = df.loc[df['number'] == str(driver_number), 'position'].iloc[0]

    return pos

def get_constructor_name(year, end_position):
    df = f1.constructor_standings(year, None)
    df.style.hide_index()
    pos = df.loc[df['position'] == str(end_position), 'name'].iloc[0]
    return pos 

def get_constructor_pos(year):
    df = f1.constructor_standings(year, None)
    pos = df[['position', 'name', 'points']]
    return pos

def get_winning_constructor(year):
    df = f1.constructor_standings(year, None)
    winner = df.loc[df['position'] == str(1), 'name'].iloc[0]
    return winner

def get_winning_driver(year):
    df = f1.driver_standings(year, None)
    winner = df.loc[df['position'] == str(1), 'driver'].iloc[0]
    return winner

def get_driver_standings(year):
    df = f1.driver_standings(year, None)   
    pos = df[['position', 'driver', 'points']]
    return pos


"""
req = input("Driver or Constructor Standings? (D/C): ")
if req=='D':
    pprint_df(get_driver_standings(int(input('Enter year: '))))
elif req=='C':
    pprint_df(get_constructor_pos(int(input('Enter year: '))))
"""


# Output a CSV file with the points and constructor name for a specific constructor over a set time period

def constructor_stats(constructor, start_year):
    constructor_points = pandas.DataFrame()

    for i in range(start_year, 2020):
        df = f1.constructor_standings(i)
        constructor_points = constructor_points.append(df.loc[df['constructorID']==constructor])

    constructor_points = constructor_points[['points', 'name']]
    fileName = "{}_points_history.csv".format(constructor)
    constructor_points.to_csv(fileName, index=False, encoding='utf-8')

constructor_stats('red_bull', 2004)
