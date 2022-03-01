
from this import d
from .utils import sorted_by_key  
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt


def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels, label = "water level data")

    """typical low and high values """
    print(station.typical_range)
    print(station)
    y_low = [station.typical_range[0]]*len(levels)

    y_high = [station.typical_range[1]]*len(levels)
    plt.plot(dates, y_low, label= " typical low")
    plt.plot(dates, y_high, label= " typical high")

    plt.xlabel('date')
    plt.ylabel('water level / m')
    plt.title('Station: '+ station.name)
    plt.show()





