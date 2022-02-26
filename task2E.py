from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
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



"""x = [1,2,3]
# corresponding y axis values
y = [2,4,1]
 
# plotting the points
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('My first graph!')
 
# function to show the plot
plt.show()"""
