from floodsystem.geo import rivers_with_stations, stations_within_radius
from floodsystem.stationdata import build_station_list

def run_task_1D(): 
    stations = build_station_list()
    
    list_of_rivers = rivers_with_stations(stations)

    return list_of_rivers

list_1D = run_task_1D()
print (list_1D)
print (len(list_1D))