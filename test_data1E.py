from floodsystem.geo import build_station_list
from floodsystem.geo import rivers_by_station_number

def test_rivers_by_station_number():
    """Tests to check that the outputs from funtion rivers_by_station_number are as expected"""
    stations = build_station_list()
    test = rivers_by_station_number(stations, 9)
    for station in test:
        assert type(station) is tuple 
        assert type(station[1]) is int
    i=0
    for i in range(0,len(test)-1):
        assert test[i][1] >= test[i+1][1]

