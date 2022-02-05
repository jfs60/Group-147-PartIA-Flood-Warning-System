# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa



from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list
from . station import MonitoringStation


def station_by_distance (stations, p):
    station_distance = []
    temp_distance = haversine(station.coordinate,p)
    
    

