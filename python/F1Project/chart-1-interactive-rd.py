import pandas as pd

df = pd.read_excel('data/R&D_Data.xlsx')

df = df.drop(columns='CAGR')
print(df)

df.to_csv('data/R&D_Data.csv')

