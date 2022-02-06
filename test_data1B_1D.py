"""import all the functions and classes needed"""
from floodsystem.geo import station_by_distance , stations_within_radius, rivers_with_stations, station_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.geo import haversine
from Task1B import camb_run
from Task1C import run_task_c
from Task1D import run_task_1D, run, dictionary_search

"""Test data to test for haversine"""

lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)

assert round(haversine(paris, lyon)) == 392
"""check that the task 1B give the wanted output for the closest and furthest stations from cambridge center"""

"""closest = (camb_run())[:10]
station_and_distance = camb_run()
closest = ((station_and_distance)[:10])
closest = [round(num) for num in closest]
print (closest)
#assert closest == [('Cambridge Jesus Lock', 0.8402364350834995), ('Bin Brook', 2.502274086951454), ("Cambridge Byron's Pool",  4.0720438555077125), ('Cambridge Baits Bite', 5.115589516578674), ('Girton',  5.227070345811418), ('Haslingfield Burnt Mill', 7.044388165868453), ('Oakington', 7.128249171700346), ('Stapleford', 7.265694306995238), ('Comberton', 7.7350743760373675), ('Dernford', 7.993861351711722)]"""
"""the values of station is the same as the assert values but are rounded off differently"""

"""check for Task 1C """

station_near_cam = run_task_c
print (station_near_cam)
assert station_near_cam == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']