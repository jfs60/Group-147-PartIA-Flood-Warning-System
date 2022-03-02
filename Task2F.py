import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

stations = build_station_list()
update_water_levels(stations)
wanted_stations = stations_level_over_threshold(stations, 0)
counter = 0 
for station in wanted_stations:
    dates, levels = fetch_measure_levels(station[0].measure_id, dt=datetime.timedelta(days=2))
    if dates == [] or levels == []:
        pass
    else:
        counter +=1
        plot_water_level_with_fit(station,dates,levels,4)
        if counter > 4:
            break
        # to ensure that the it only gives the top 5 stations

