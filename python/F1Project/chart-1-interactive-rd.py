# Accessing excel file which has manually entered data and converting it to a csv file for chart 1

import pandas as pd

"""df = pd.read_excel('data/R&D_Data.xlsx')

print(df)

df.to_csv('data/f1_rd_data.csv')
"""

df = pd.read_excel('data/rd_source_list.xlsx')

df.to_csv('data/rd_source_list.csv')