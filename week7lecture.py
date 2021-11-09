import requests
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate


def pprint_df(dframe):
    print(tabulate(dframe, headers='keys', tablefmt='psql', showindex=False))


# Double/multiple nesting in json:

"""
url ='https://api.worldbank.org/v2/country/GBR/indicator/SP.POP.TOTL?format=json'
html = requests.get(url)

json_data = html.json()
good_data = json_data[1]

df = pd.DataFrame(good_data)

df[['date', 'value']].to_csv('my_csv_file.csv')
"""



# Scraping
"""
url='https://www.comparethemarket.com/car-insurance/content/global-supercar-index/'

html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')

table = soup.find('div', id='cheapest-countries')
headings = table.findAll('h4')
values=table.findAll('p', class_='lead')

headings_list = [i.text for i in headings]

values_list = [i.text for i in values]

values_list = [int(i.text.replace('£', '').replace(',', '')) for i in values]

df = pd.DataFrame([headings_list, values_list]).T
print(df)

"""

url='https://www.bloomberg.com/billionaires/'

html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')

table = soup.find('div', class_="dvz-content")
print(table)
#headings = table.findAll('div', class_="table-cell t-name")
#values=table.findAll('div', class_='table-cell active t-nw')

#headings_list = [i.text for i in headings]

#values_list = [i.text for i in values]


#df = pd.DataFrame([headings_list, values_list]).T
#print(df)