# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    #task 1f
    def typical_range_consistent(self):
            """returns true if and only if the data in the station class meets certain consistency
            requirements including that typical highs are higher than lows and that data is available
            also checks if latest level is consistent to save a lot of other code
            """
            if self.typical_range is None:
                return False

            # the following if statement is probably not necessary as math.isnan
            # covers it, but it does no harm.

            if self.typical_range[0] is None or self.typical_range[1] is None:
                return False

            if math.isnan(self.typical_range[0]) or math.isnan(self.typical_range[1]):
                return False

            low, high = self.typical_range
            # using this phrasing to make it more clear how consistency is being
            # checked
            return not (high < low)


def inconsistent_typical_range_stations(stations):
    """Returns a list of all stations with inconsistent typical ranges"""
    return [s for s in stations if not s.typical_range_consistent()]