"""import all the functions and classes needed"""
from floodsystem.geo import station_by_distance , stations_within_radius, rivers_with_stations, station_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.geo import haversine
from Task1B import camb_run
from Task1C import run_task_c
from Task1D import run_task_1D, run, dictionary_search
"""check for Task 1C """

station_near_cam = run_task_c()
print (station_near_cam)
assert station_near_cam == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
""" there is no assertion error therefore the code run is correct"""