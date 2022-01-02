import pandas as pd

df = pd.read_excel('data/R&D_Data.xlsx')

print(df)

df.to_csv('data/f1_rd_data.csv')

