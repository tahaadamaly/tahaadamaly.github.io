import pandas as pd
import formula1 as f1

master_data = pd.DataFrame()

race_country = ['Bahrain', 'Italy', 'Portugal', 'Spain', 'Monaco', 'Azerbaijan', 'France', 'Austria', 'Austria', 'Great Britain', 'Hungary', 'Belgium', 'Netherlands', 'Italy',
'Russia', 'Turkey', 'United States', 'Mexico', 'Brazil', 'Qatar', 'Saudi Arabia']


# Create master data set with all driver standings for each race in 2021 (21 races)
for i in range(1, 22):
    df = f1.driver_standings(2021, i)
    df = df[['driver', 'points', 'driverID']]
    df['race'] = i
    df['race_country'] = race_country[i-1]
    master_data = master_data.append(df)

# Delete any drivers not in the top 10 as of round 21

top_ten_drivers = ['max_verstappen', 'hamilton', 'bottas', 'perez', 'leclerc', 'norris', 'sainz', 'ricciardo', 'gasly', 'alonso']

for x in master_data['driverID']:
    if x not in top_ten_drivers:
        master_data.drop(master_data.index[master_data['driverID'] == x], inplace=True)

master_data = master_data[master_data['driverID'].isin(top_ten_drivers)]

print(master_data.head(15))


#master_data.to_csv('data/f1_2021_driver_points.csv')
master_data.to_csv('data/f1_2021_top_driver_points.csv')


