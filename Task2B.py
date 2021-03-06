from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Running for Task 2B"""

    stations = build_station_list()
    update_water_levels(stations)
    tol=0.8

    flooded_stations=stations_level_over_threshold(stations,tol)
   
    return flooded_stations

station_that_are_flooding = run()
print (station_that_are_flooding)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()