from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.geo import haversine

def run_task_c(): 

    stations = build_station_list()

    camb = (52.2053, 0.1218) 
    list_1C = stations_within_radius(stations, camb, 10)

    
    return list_1C

#list_of_stations_within_radius = run_task_c()
#print (list_of_stations_within_radius)    