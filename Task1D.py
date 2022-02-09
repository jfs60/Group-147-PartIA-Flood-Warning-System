from floodsystem.geo import rivers_with_stations, station_by_river, stations_within_radius
from floodsystem.stationdata import build_station_list

def run_task_1D(): 
    stations = build_station_list()
    
    list_of_rivers = rivers_with_stations(stations)

    return list_of_rivers

list_1D = run_task_1D()

myList = sorted(list(list_1D))

print (myList[:10])
print (len(myList))

def run(): 
    stations = build_station_list()

    station_river_dict = station_by_river(stations)

    return station_river_dict

dict_river_station = run()


def dictionary_search (dict_river_station, river): 
    list_for_dict = []
    for dict in dict_river_station.keys():
        if (dict == river):
            dictionary = dict_river_station[dict]

    return dictionary

print(dictionary_search(dict_river_station, "River Cam"))
print(dictionary_search(dict_river_station, "River Aire"))
print(dictionary_search(dict_river_station, "River Thames"))


