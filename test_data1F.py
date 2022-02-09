from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def test_inconsistent_typical_range_stations():
    stations = build_station_list()
    r2 = inconsistent_typical_range_stations(stations)
    for i in stations:
        for j in r2:
            if i.name == j:
                assert i.typical_range == None or i.typical_range[1] - i.typical_range[0] < 0
