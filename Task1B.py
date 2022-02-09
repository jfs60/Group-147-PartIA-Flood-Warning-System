""" import all the functions from the different files"""
from floodsystem.geo import station_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.geo import haversine

"""run the function for task 1B"""
def camb_run (): 
    stations = build_station_list()

    camb = (52.2053, 0.1218) 
    distance = station_by_distance(stations, camb)
    
    return distance

station_and_distance = camb_run()
closest = (camb_run())[:10]
print(closest)
furthest = (camb_run())[-10:]
print (furthest)