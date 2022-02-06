from floodsystem.geo import station_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.geo import haversine

#test haversine
lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)
assert haversine(camb, lyon)) == 392.2172595594006
