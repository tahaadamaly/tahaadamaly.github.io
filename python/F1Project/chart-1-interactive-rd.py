# Accessing excel file which has manually entered data and converting it to a csv file for chart 1

import pandas as pd

df = pd.read_excel('data/R&D_Data.xlsx')


# This calculates the sum of expenditure based on the year and creates a new column with this total expenditure for each year
def categorise(row):
    return df.loc[df['year']==row['year'], 'expenditure'].sum()
df['totalexp'] = df.apply(lambda row: categorise(row), axis=1)

# This calculates the proportion of total expenditure each team spends per year
df['proptotalexp'] = df['expenditure']/df['totalexp']

df.to_csv('data/f1_rd_data.csv')
