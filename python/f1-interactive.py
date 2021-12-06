import pandas as pd
import formula1 as f1

master_data = pd.DataFrame()

top_ten_drivers = ['max_verstappen', 'hamilton', 'bottas', 'perez', 'leclerc', 'norris', 'sainz', 'ricciardo', 'gasly', 'alonso']


for i in range(1, 22):
    df = f1.driver_standings(2021, i)
    df = df[['driver', 'points', 'driverID']]
    df['race'] = i
    master_data = master_data.append(df)


for x in master_data['driverID']:
    if x not in top_ten_drivers:
        master_data.drop(master_data.index[master_data['driverID'] == x], inplace=True)
print(master_data)




master_data.to_csv('data/f1_2021_top_driver_points.csv')