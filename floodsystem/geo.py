# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list

#create a haversine function that calculate distance between two coordinates
from math import radians, degrees, sin, cos, asin, acos, sqrt
def haversine (coordinate_1, coordinate_2): 
    distance = 6371 * (acos(sin(coordinate_1[0])) * sin(coordinate_2[0]) 
        + cos(coordinate_1[0]) * cos(coordinate_2[0]) * cos(coordinate_1[1] - coordinate_2[1]))
    return distance

# p is a tuple 

#Task1B geocode
def station_by_distance (stations, p):
    station_distance = []
    assert len(p)== 2 
    for station in stations:
        temp_tuple = ()
        temp_distance = haversine(station.coord, p)
        temp_tuple = (station.name, temp_distance)
        station_distance.append(temp_tuple)
    station_distance = sorted_by_key(station_distance, 1)
    return station_distance

#Task1C geocode
def stations_within_radius (stations, centre, r): 
    list_of_station_in_radius = []
    assert len(centre) == 2
    string_temp = ""
    for station in stations:
        temp_distance = haversine(station.coord, centre)
        if temp_distance <= r : 
            string_temp = (station.name)
            list_of_station_in_radius.append(string_temp)
        
        
        
        list_of_station_in_radius =  sorted(list_of_station_in_radius)

        
    
    return list_of_station_in_radius




    

