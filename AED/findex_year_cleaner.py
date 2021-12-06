import pandas as pd

df = pd.read_excel('AED/globfindex.xlsx')
df.rename(columns={'Unnamed: 0': 'Year', 'Unnamed: 1': 'Country Code', 'Unnamed: 2': 'Country Name'}, inplace=True)
df = df[df['Year'] == 2014]
df.to_excel('AED/cleanedfindex.xlsx')