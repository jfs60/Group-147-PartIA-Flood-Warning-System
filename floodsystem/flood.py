from this import d
from .utils import sorted_by_key  
from floodsystem.stationdata import build_station_list

def stations_level_over_threshold (stations, tol): 
    stations_flooded = []

    for station in stations: 
        relative_level = station.relative_water_level()
        
        try:
            if relative_level > tol:
                stations_flooded.append((station.name, relative_level))
        except:
            pass

        

    stations_flooded.sort(key=lambda x: x[1], reverse=True)


    return stations_flooded

def stations_highest_rel_level(stations, N ): 
    station_list  = []
    
    station_flooded = stations_level_over_threshold (stations, 0)
    for i in range (N): 
        station = station_flooded[i]
        station_list.append(station)


    return (station_list)

        
