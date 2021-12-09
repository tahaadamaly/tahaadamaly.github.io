import pandas as pd
import formula1 as f1

master_data = pd.DataFrame()

top_ten_drivers = ['max_verstappen', 'hamilton', 'bottas', 'perez', 'leclerc', 'norris', 'sainz', 'ricciardo', 'alonso', 'gasly']
race_country = ['Bahrain', 'Italy', 'Portugal', 'Spain', 'Monaco', 'Azerbaijan', 'France', 'Austria', 'Austria', 'Great Britain', 'Hungary', 'Belgium', 'Netherlands', 'Italy',
'Russia', 'Turkey', 'United States', 'Mexico', 'Brazil', 'Qatar', 'Saudi Arabia']


for i in range(2000, 2022):
    df = f1.constructor_standings(i)
    df = df[['name', 'points', 'constructorID']]
    df['year'] = i
    master_data = master_data.append(df)


print(master_data)

master_data.to_csv('data/f1_constr_points_yearly.csv')





