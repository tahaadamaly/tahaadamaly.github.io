from os import name
from bs4.element import DEFAULT_OUTPUT_ENCODING
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Setup
url='https://www.autosport.com/f1/standings/'

html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')

# Finding table column with drivers and table column with points
soup_drivers = soup.find_all("td", class_='ms-table_cell ms-table_field--driver')
soup_points = soup.find_all("td", class_='ms-table_cell ms-table_field--total_points')

points = {}

# Appending drivers and their points into a python dictionary, with the key being the driver and the value being the points
for i in range(0, len(soup_drivers)):
    points[soup_drivers[i].text] = soup_points[i].text

# Take scraped data and create dataframe with cleaned data
points_items = points.items()
data_list = list(points_items)
points_df = pd.DataFrame(data_list)
points_df = points_df.rename(columns={0: 'driver', 1: 'points'})

# Cleaning the spaces at the beginning and end of the name and points (4 spaces before name, 3 spaces after)
name_change = {}
for i in points_df.values:
    new_name = i[0].replace('    ', '')
    name_change[i[0]] = new_name

for i in range(0, len(points_df['driver'])):
    points_df['driver'][i] = points_df['driver'][i].replace('    ', '')
    points_df['driver'][i] = points_df['driver'][i].replace('   ', '')

points_df.drop(points_df.tail(11).index,
        inplace = True)

# Export to CSV to be used in a vegalite specification
points_df.to_csv('data/w7_f1_points.csv')

