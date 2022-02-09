from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
stations = build_station_list()
print("\n"+str(rivers_by_station_number(stations,7))+"\n")

