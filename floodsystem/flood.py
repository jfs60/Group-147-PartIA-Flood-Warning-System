from .utils import sorted_by_key

#Task2B
def stations_level_over_threshold(stations, tol):
    """Function which takes the list of all stations and a tolerance level. Returns a tuple of station name and relative water level for stations
    who's relative water level is over the tol """
    stations_over_tol = []
    for station in stations:
        if station.relative_water_level() == None:
            pass
        elif station.relative_water_level() > tol:
            stations_over_tol.append((station.name, station.relative_water_level()))

    sorted_stations_over_tol = sorted_by_key(stations_over_tol,1,True)
    return sorted_stations_over_tol


#Task2C
def stations_highest_rel_level(stations, N):
    """Takes a list of all monitoring stations and a number N as an input. Returns the top N stations with the highest relative water level as a tuple of station name and relative water level. Shows the station most vulnerable to flooding """
    level_relative_to_range = stations_level_over_threshold(stations,0)
    #list is already sorted in the stations level over threshold function
    return level_relative_to_range[:N]


#Task2E
def stations_level_over_threshold_class(stations, tol):
    """Function which takes the list of all stations and a tolerance level. Returns a class of the station information of station for stations
    who's relative water level is over the tol """
    stations_over_tol = []
    for station in stations:
        if station.relative_water_level() == None:
            pass
        elif station.relative_water_level() > tol:
            stations_over_tol.append((station, station.relative_water_level()))

    sorted_stations_over_tol = sorted_by_key(stations_over_tol,1,True)
    return sorted_stations_over_tol

def stations_highest_rel_level_class(stations, N):
    """Takes a list of all monitoring stations and a number N as an input. Returns the top N stations with the highest relative water level as a tuple of station name and relative water level. Shows the station most vulnerable to flooding """
    level_relative_to_range = stations_level_over_threshold_class(stations,0)
    #list is already sorted in the stations level over threshold function
    return level_relative_to_range[:N]
        
