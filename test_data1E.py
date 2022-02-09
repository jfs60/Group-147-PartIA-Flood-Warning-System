"""import all the functions and classes needed"""
from floodsystem.geo import  rivers_by_station_number
from Task1E import rivers_by_station_number
from floodsystem.stationdata import build_station_list

stations = build_station_list()
def test_rivers_by_station_number():
    N = 9
    result = rivers_by_station_number(stations, N)
    assert len(result) >= 9
