# Accessing excel file which has manually entered data and converting it to a csv file for chart 1

import pandas as pd

df = pd.read_excel('data/R&D_Data.xlsx')

print(df)

def categorise(row):
    return df.loc[df['year']==row['year'], 'expenditure'].sum()
df['totalexp'] = df.apply(lambda row: categorise(row), axis=1)
df['proptotalexp'] = df['expenditure']/df['totalexp']



df.to_csv('data/f1_rd_data.csv')
