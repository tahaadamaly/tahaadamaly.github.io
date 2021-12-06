import pandas as pd

df = pd.read_excel('AED/CleanedFiles/cleanedfininfra.xlsx')
varlist = pd.read_excel('AED/RawData/varlist.xlsx')

codes_needed = []

for x in varlist['Country Code - Needed']:        
    codes_needed.append(x)

codes_needed = codes_needed[:-19]

for i in df['ISO-3 code']:
    if i not in codes_needed:
        df.drop(df.index[df['ISO-3 code'] == i], inplace=True)

df.to_excel('AED/cleanedfininfra2.xlsx')

