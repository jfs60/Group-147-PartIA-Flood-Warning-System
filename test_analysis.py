from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy

stations = build_station_list()
station = stations[3]
def test_polyfit():
        dt=1
        p=4
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        # try and remove empty list problem with Letcombe Bassett
        if dates == [] or levels == []:
            pass
        else:
            poly, x1 = polyfit(dates, levels, p)
            assert isinstance(poly, numpy.poly1d)
            assert isinstance(x1, float)