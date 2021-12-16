import fastf1 as ff1
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from fastf1 import plotting
import numpy as np

plotting.setup_mpl()
ff1.Cache.enable_cache('python/cache')


race = ff1.get_session(2021, 'Saudi Arabia', 'R')
laps = race.load_laps(with_telemetry=True)

ver_lap = laps.pick_driver('VER')
ver_lap_37 = ver_lap.loc[ver_lap['LapNumber'] == 37]
ham_lap = laps.pick_driver('HAM')
ham_lap_37 = ham_lap.loc[ham_lap['LapNumber'] == 37]

ver_tel = ver_lap_37.get_car_data().add_distance()
ham_tel = ham_lap_37.get_car_data().add_distance()

ver_tel = pd.DataFrame(ver_tel)
ham_tel = pd.DataFrame(ham_tel)

ver_tel['Time'] = ver_tel['Time'].apply(lambda x: x / np.timedelta64(1, 's'))
ham_tel['Time'] = ham_tel['Time'].apply(lambda x: x / np.timedelta64(1, 's'))

#def calc_accel(speed_list, time_list):

# ver_tel['Acceleration'] = calc_accel(ver_tel['Speed'], ver_tel['Time'])

print(ver_tel['Speed'][0])