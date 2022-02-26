from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

def run (): 
    stations = build_station_list()
    update_water_levels(stations)

    list = stations_highest_rel_level(stations, 9) 
    return(list)

stations_Task_2C = run()
print (stations_Task_2C)
