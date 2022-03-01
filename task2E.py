from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

def run ():
    stations = build_station_list()
    update_water_levels(stations)

    Number_of_stations = 5
    dt = 10

    stations_flooded = stations_highest_rel_level(stations, Number_of_stations)  
    
    for station in stations_flooded:
        station=station[0]
        dates, level = fetch_measure_levels(station.measure_id,dt=timedelta(days=dt))
        
        if len(dates) == 0 or len(level)== 0: 
            continue
        print(len(dates))
        
        print (len(level))
        plot_water_levels(station, dates, level)

run()



