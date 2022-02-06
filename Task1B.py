from floodsystem.geo import station_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.geo import haversine
#camb = (52.2053, 0.1218)
#lyon = (43.567, 55.333) 
#print(haversine(camb, lyon))

def camb_run (): 
    stations = build_station_list()

    camb = (52.2053, 0.1218) 
    distance = station_by_distance(stations, camb)
    
    return distance

closest = (camb_run())[:10]
print (closest)
furthest = (camb_run())[-10:]
print (furthest)