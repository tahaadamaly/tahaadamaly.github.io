import requests
import json
import time

apibase = "https://api.nomics.com/v1/exchange-rates/history?key=09a184e1807679b00d552874f6257bf2c615a327&currency={}&start=2010-04-14T00%3A00%3A00Z&end=2021-09-14T00%3A00%3A00Z"
coinlist = ['BTC', 'ETH', 'USDT', 'SOL']
fileBase = "crypto_{}_history.json"

# API Fetch for 4 different cryptocurrencies from the Nomics API

for i in coinlist:
    apiurl = apibase.format(i)
    data = requests.get(apiurl).json()
    fileName = fileBase.format(i)
    with open(fileName, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    time.sleep(1)




