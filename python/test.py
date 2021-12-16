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



# Saudi Arabia Lap 37 Telemetry
ver_lap = laps.pick_driver('VER')
ver_lap_37 = ver_lap.loc[ver_lap['LapNumber'] == 37]
ham_lap = laps.pick_driver('HAM')
ham_lap_37 = ham_lap.loc[ham_lap['LapNumber'] == 37]

ver_tel = ver_lap_37.get_car_data().add_distance()
ham_tel = ham_lap_37.get_car_data().add_distance()


rbr_color = ff1.plotting.team_color('RBR')
mer_color = ff1.plotting.team_color('MER')

fig, ax = plt.subplots(3)
plt.suptitle("Saudi Arabia Lap 37 Analysis")

ver_tel = pd.DataFrame(ver_tel)
ham_tel = pd.DataFrame(ham_tel)



ver_tel['Time'] = ver_tel['Time'].apply(lambda x: x / np.timedelta64(1, 's'))
ham_tel['Time'] = ham_tel['Time'].apply(lambda x: x / np.timedelta64(1, 's'))

accel_list = []
for i in range(0, 397):
    accel_list.append((((ver_tel['Speed'].iloc[i+1] - ver_tel['Speed'].iloc[i])*(10/36))/(ver_tel['Time'].iloc[i+1] - ver_tel['Time'].iloc[i]))/9.81)
accel_list.append(0)
ver_tel['Acceleration'] = accel_list


accel_list1 = []
for i in range(0, 403):
    accel_list1.append((((ham_tel['Speed'].iloc[i+1] - ham_tel['Speed'].iloc[i])*(10/36))/(ham_tel['Time'].iloc[i+1] - ham_tel['Time'].iloc[i]))/9.81)
accel_list1.append(0)

ham_tel['Acceleration'] = accel_list1


ax[0].plot(ver_tel['Time'], ver_tel['Speed'], color=rbr_color, label='VER')
ax[0].plot(ham_tel['Time'], ham_tel['Speed'], color=mer_color, label='HAM')
ax[0].set_ylabel('Speed in km/h')
ax[0].legend(loc='lower right')

ax[1].plot(ver_tel['Time'], ver_tel['Throttle'], color=rbr_color, label='VER')
ax[1].plot(ham_tel['Time'], ham_tel['Throttle'], color=mer_color, label='HAM')
ax[1].set_ylabel('Throttle')

ax[2].plot(ver_tel['Time'], ver_tel['Acceleration'], color=rbr_color, label='VER')
ax[2].plot(ham_tel['Time'], ham_tel['Acceleration'], color=mer_color, label='HAM')
ax[2].set_ylabel('Brakes')


plt.show()




"""fast_ver = laps.pick_driver('VER').pick_fastest()
ver_car_data = fast_ver.get_car_data().add_distance()
t1 = ver_car_data['Distance']
vCar1 = ver_car_data['Speed']

fast_ham = laps.pick_driver('HAM').pick_fastest()
ham_car_data = fast_ham.get_car_data().add_distance()
t2 = ham_car_data['Distance']
vCar2 = ham_car_data['Speed']


fig, ax = plt.subplots()
ax.plot(t1, vCar1, label='VER')
ax.plot(t2, vCar2, label='HAM')
ax.set_xlabel('Distance')
ax.set_ylabel('Speed [KM/H]')
ax.set_title('Max vs Lewis Fastest Race Lap - Abu Dhabi 2020')
ax.legend()
plt.show()"""


