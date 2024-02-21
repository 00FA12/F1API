from matplotlib import pyplot as plt
import fastf1
session = fastf1.get_session(2023, 'Monaco', 'Q')
session.load()
fast_alonso = session.laps.pick_driver('ALO').pick_fastest()
fast_ver = session.laps.pick_driver('VER').pick_fastest();

aloCarData = fast_alonso.get_car_data()
verCarData = fast_ver.get_car_data()
t = aloCarData['Time']
t2 = verCarData['Time']
vCar = aloCarData['Speed']
vCar2 = verCarData['Speed']
fig, ax = plt.subplots()
ax.plot(t, vCar, label='Alo')
ax.plot(t2, vCar2, label='Ver')
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Monaco Q')
ax.legend()
plt.show()