import json
import pandas as pd
import numpy as np

# Creating a function to calculate z-score given an x value and a dataset
def z_score(x, dataset):
    return((x-np.mean(dataset))/np.std(dataset))

# Open both consumption datasets for denmark and sweden
with open('data/fred_consump_DNKPFCEQDSMEI.json') as jsonFile:
    den_data = json.load(jsonFile)
    jsonFile.close()

with open('data/fred_consump_SWEPFCEQDSMEI.json') as jsonFile2:
    swe_data = json.load(jsonFile2)
    jsonFile2.close()

# Setting up variables
denmark_values = []
sweden_values = []
denmark_values_rebased = []
sweden_values_rebased = []
den_dates = []
swe_dates = []

sweden_dataset = {}
denmark_dataset = {}

# Sweden data rebasing
for i in swe_data['observations']:
    swe_dates.append(i['date'])
    sweden_values.append(float(i['value']))

for y in sweden_values:
    sweden_values_rebased.append(z_score(y, sweden_values))

for r in range(len(swe_dates)):
    sweden_dataset[swe_dates[r]] = sweden_values_rebased[r]


# Denmark data rebasing
for n in den_data['observations']:
    den_dates.append(n['date'])
    denmark_values.append(float(n['value']))

for z in denmark_values:
    denmark_values_rebased.append(z_score(z, denmark_values))

for e in range(len(den_dates)):
    denmark_dataset[den_dates[e]] = denmark_values_rebased[e]

# Combine data into pandas dataframes
den_data_items = denmark_dataset.items()
den_data_list = list(den_data_items)
denmark_df = pd.DataFrame(den_data_list)

swe_data_items = sweden_dataset.items()
swe_data_list = list(swe_data_items)
sweden_df = pd.DataFrame(swe_data_list)

denmark_df.rename(columns={0 : 'date', 1: 'value'}, inplace=True)
sweden_df.rename(columns={0 : 'date', 1: 'value'}, inplace=True)

# Export to CSV's to be used in a vegalite specification
denmark_df.to_csv('data/den_values_rebased.csv')
sweden_df.to_csv('data/swe_values_rebased.csv')