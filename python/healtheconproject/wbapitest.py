import wbgapi as wb
import pandas as pd

temp = []
for row in wb.data.fetch('SP.DYN.CDRT.IN'):
    temp.append([row['economy'], row['time'], row['value']])

temp = pd.DataFrame(temp)
temp.rename(columns={0: 'country', 1: 'year', 2: 'death_rate'}, inplace=True)
print(temp)

#temp.to_excel('tempfile.xlsx')