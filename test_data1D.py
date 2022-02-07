"""import all the functions and classes needed"""
from floodsystem.geo import station_by_distance , stations_within_radius, rivers_with_stations, station_by_river
from floodsystem.stationdata import build_station_list
from floodsystem.geo import haversine
from Task1B import camb_run
from Task1C import run_task_c
from Task1D import run_task_1D, run, dictionary_search, dict_river_station

list_1D = run_task_1D()

myList = sorted(list(list_1D))
assert (myList[:10]) == ['Addlestone Bourne', 'Aire Washlands', 'Alconbury Brook', 'Aldingbourne Rife', 'Aller Brook', 'Allison Dyke', 'Alverthorpe Beck', 'Ampney Brook', 'Amwell Loop', 'Arkle Beck']
assert len(myList) == 950

""" No assertion error """
assert (dictionary_search(dict_river_station, "River Aire")) == ['Airmyn', 'Apperley Bridge', 'Armley', 'Beal Weir Bridge', 'Bingley', 'Birkin Holme Washlands', 'Carlton Bridge', 'Castleford', 'Chapel Haddlesey', 'Cononley', 'Cottingley Bridge', 'Ferrybridge Lock', 'Fleet Weir', 'Gargrave', 'Kildwick', 'Kirkstall Abbey', 'Knottingley Lock', 'Leeds Crown Point', 'Leeds Crown Point Flood Alleviation Scheme', 'Leeds Knostrop Weir Flood Alleviation Scheme', 'Oulton Lemonroyd', 'Saltaire', 'Snaygill', 'Stockbridge']
"""dictionary is implemented correctly as there is no assertion error"""