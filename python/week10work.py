import requests, pandas as pd
import numpy as np

url ='https://api.beta.ons.gov.uk/v1/datasets/index-private-housing-rental-prices/editions/time-series/versions/13/observations?time=*&geography=E12000007&indexandyearchange=index'
html = requests.get(url)
json_data = html.json()

observations = json_data['observations']

empty_data = []

for x in observations:
    #print(x['dimensions']['Time']['label'], x['observation'])
    dummy = {'time': x['dimensions']['Time']['label'], 'value': x['observation']}
    empty_data.append(dummy)

df = pd.DataFrame(empty_data)

df['value'] = df['value'].astype(float)

df['month']=df['time'].str.split('-').str[0]
df['year']=df['time'].str.split('-').str[1]
df['year']='20'+df['year']
df['day']='01'

df['date']=pd.to_datetime(df['year'] + '-' +df['month'] + '-' +df['day'])
df['date']=df['date'].astype(str)

print(df.head(2))