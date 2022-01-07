import requests
import json
import time

apibase = "https://api.stlouisfed.org/fred/series/observations?series_id={}&api_key=2677c7ef979aaca29feb223566280265&file_type=json&observation_start=2019-08-01&observation_end=2021-08-01"
serieslist = ['SWEPFCEQDSMEI', 'DNKPFCEQDSMEI']
fileBase = "fred_consump_{}.json"

# API Fetch for Sweden and Denmark consumption

for i in serieslist:
    apiurl = apibase.format(i)
    data = requests.get(apiurl).json()
    fileName = fileBase.format(i)
    with open('data/{}'.format(fileName), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    # Time delay is added because the API doesn't seem to be able to handle 4 rapid requests, as an error occurs unless this delay is added
    time.sleep(1)




