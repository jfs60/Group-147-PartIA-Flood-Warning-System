from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from datetime import datetime, timedelta
import datetime
import matplotlib.pyplot as plt
import numpy as np

def run ():
    stations = build_station_list()
    update_water_levels(stations)

    Number_of_stations = 5
    dt = 10

    stations_flooded = stations_highest_rel_level(stations, Number_of_stations) 

    flooded_stations= []
    for station in stations_flooded:
        for station_1 in stations: 

            if station_1.name ==station[0]: 
                flooded_stations.append(station_1)
    

    
    for station in flooded_stations:
        dates, level = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))
        
        
        if len(dates) == 0 or len(level)== 0: 
            continue
        print(dates) 
        
        print (level)
        plt.plot(dates, level)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('My first graph!')
        plt.show
        #plot_water_levels(station, dates, level)
        #plt.show 

run()



t = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5)]
level = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

# Plot
plt.plot(t, level)


# Add axis labels, rotate date labels and add plot title
plt.xlabel('date')
plt.ylabel('water level (m)')
plt.xticks(rotation=45);
plt.title("Station A")

# Display plot
plt.tight_layout()  # This makes sure plot does not cut off date labels

plt.show()