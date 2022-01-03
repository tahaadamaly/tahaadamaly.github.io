import pandas as pd
import formula1 as f1

master_data = pd.DataFrame()

for i in range(2000, 2022):
    df = f1.constructor_standings(i)
    df = df[['name', 'points', 'constructorID']]
    df['year'] = i
    master_data = master_data.append(df)


print(master_data)

#master_data.to_csv('data/f1_constr_points_yearly.csv')





