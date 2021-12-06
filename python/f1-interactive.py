import pandas as pd
import formula1 as f1

master_data = pd.DataFrame()

for i in range(1, 22):
    df = f1.driver_standings(2021, i)
    df = df[['driver', 'points']]
    df['race'] = i
    master_data = master_data.append(df)

master_data.to_csv('data/f1_2021_driver_points.csv')