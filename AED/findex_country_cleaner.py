import pandas as pd

df = pd.read_excel('AED/cleanedfindex.xlsx')
varlist = pd.read_excel('AED/varlist.xlsx')

codes_needed = []

for x in varlist['Country Code - Needed']:        
    codes_needed.append(x)

codes_needed = codes_needed[:-19]

for i in df['Country Code']:
    if i not in codes_needed:
        df.drop(df.index[df['Country Code'] == i], inplace=True)

#df.to_excel('AED/cleanedfindex2.xlsx')

