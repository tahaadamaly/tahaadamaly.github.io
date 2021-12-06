import pandas as pd

df = pd.read_excel('AED/Financial infrastructure data.xlsx')
df = df[df['Year'] == 2014]
df.to_excel('AED/cleanedfininfra.xlsx')