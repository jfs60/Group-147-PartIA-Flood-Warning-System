from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold, stations_highest_rel_level_class
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

    stations_flooded = stations_highest_rel_level_class(stations, Number_of_stations)  
    
    for station in stations_flooded:
        dates, level = fetch_measure_levels(station[0].measure_id,dt=datetime.timedelta(days=dt))
        
        if len(dates) == 0 or len(level)== 0: 
            continue
        print(len(dates))
        
        print (len(level))
        plot_water_levels(station, dates, level)

if __name__=="__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")

    # Run Task2E
    run()

