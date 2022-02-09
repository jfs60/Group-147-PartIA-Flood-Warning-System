# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
''' import all the classes and functions needed for this page'''
from this import d
from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list

"""create a haversine function that calculate distance between two coordinates
- takes two coordinates as parameters 
- returns the distance between two coordinates"""
from math import radians, degrees, sin, cos, asin, acos, sqrt, pi
def haversine (coordinate_1, coordinate_2): 
    lat1, lon1 = coordinate_1
    lat2, lon2 = coordinate_2 
    lon1 = pi*lon1/180
    lon2 = pi*lon2/180
    lat1 = pi*lat1/180
    lat2 = pi*lat2/180
    distance = 6371*2*asin(sqrt((sin((lat1-lat2)/2))**2+cos(lat1)*cos(lat2)*(sin((lon1-lon2)/2))**2))
    return distance



#Task1B geocode
"""define a function that gives a list of station and their distance 
- takes in a list of stations and a tuple p as parameters (check in the function if p is a tuple)
- return a sorted list of name of station and the distance from the tuple 
"""
def station_by_distance (stations, p):
    station_distance = []
    #check if p is a tuple
    assert len(p)== 2 
    for station in stations:
        temp_tuple = ()
        temp_distance = haversine(station.coord, p)
        temp_tuple = (station.name, temp_distance)
        station_distance.append(temp_tuple)
    station_distance = sorted_by_key(station_distance, 1)
    return station_distance

#Task1C geocode
""" define a function that gives a list of stations that are within the radius 
- takes in a list of stations as the input, a centre coordinate and a radius from that centre point 
- returns a list stations in range of the centre that is sorted"""
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


#Task1D geo
"""This functions creates a set of river from the list of stations 
- it takes in the data of the stations 
- it outputs a list of data of stations"""


def rivers_with_stations (stations): 
    river_set = set()
    for station in stations:
        river_temp = station.river 
        river_set.add(river_temp)
        
    
    return river_set


"""this function outputs a dictionary that have rivers linked with the stations that are linked with the river 
- takes in the list of stations 
- outputs the dictionary linking rivers and stations"""
 
def station_by_river(stations): 
    station_by_river_dict = {}
    
    for station in stations: 
        
        if station.river in station_by_river_dict : 
            station_by_river_dict[station.river].append(station.name)
            station_by_river_dict[station.river].sort()
        else: 
            station_by_river_dict[station.river] = [station.name]


    return station_by_river_dict

#Task 1E
def rivers_by_station_number(stations, N):
    river_number_of_station=[]
    river_dictionary = station_by_river(stations)
    for key in river_dictionary.keys():
        number_of_stations = len(river_dictionary[key])
        river_number = key, number_of_stations
        river_number_of_station.append(river_number)
    sorted_river_number = sorted_by_key(river_number_of_station, 1, reverse=True)

    n = 0
    if sorted_river_number[N][1] == sorted_river_number[N+1][1]:
        n = 0
        while sorted_river_number[N][1] == sorted_river_number[N+n+1][1]:
            n+=1
        return sorted_river_number[:N+n]
    elif sorted_river_number[N][1] != sorted_river_number[N+1][1]: 
        return sorted_river_number[:N]
    