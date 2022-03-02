
from floodsystem.plot import *
from floodsystem.stationdata import build_station_list, update_water_levels


def test_plot_water_levels():
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.name == 'Cam':
            station_cam = station
            assert isinstance(station_cam, list)
        else:
            break