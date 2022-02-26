from this import d
from .utils import sorted_by_key  
from floodsystem.stationdata import build_station_list

def stations_level_over_threshold (stations, tol): 
    stations_flooded = []

    for station in stations: 
        relative_level = station.relative_water_level()
        print(relative_level)
        try:
            if relative_level > tol:
                stations_flooded.append((station.name, relative_level))
        except:
            pass

        

    stations_flooded.sort(key=lambda x: x[1], reverse=True)


    return stations_flooded

def stations_highest_rel_level(stations, N): 
    station_list = []
    
    for station in stations: 
        relative_level = station.relative_water_level()
        
        print(relative_level)
        if relative_level != None: 
            station_list.append ((station.name, relative_level))
        
    station_list.sort(key=lambda x: x[1], reverse=True)
    station_list = station_list[:N]
    return station_list





        
