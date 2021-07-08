""" A function that solves the most suitable (with most power) link station for a device at
given point [x,y]."""

import math


class Point:
    """Point class provide a point in 2-dimensional space."""

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __str__(self):

        return f"{self.x},{self.y}"

    def get_distance_to(self, other):
        """
        A link station’s power can be calculated:
        power = (reach - device's distance from linkstation)^2
        if distance > reach, power = 0
        Get distance to given Point.
        """
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)

class Device(Point):
    __doc__ += Point.__doc__


    def _str_best_link_station_with_power(self, best_station, power):

        if power:
            return f"Best link station for a point {self} is " + \
                f"{best_station} with power {power}\n"
        return f"No link station within reach for a point {self}\n"

    def get_best_link_station_with_power(self, link_stations):
        """
        Get best link station (with most power) for this device.
        """
        best_power = 0
        best_station = link_stations[0]
        for station in link_stations:
            power = station.get_power(self)
            if power > best_power:
                best_station = station
                best_power = power
        return self._str_best_link_station_with_power(best_station, best_power)

class LinkStation(Point):

    __doc__ += Point.__doc__

    def get_power(self, point):

        distance = self.get_distance_to(point)
        return (self.reach - distance)**2 if distance < self.reach else 0

    def __init__(self, x, y, reach):

        Point.__init__(self, x, y)
        self.reach = reach

def run_for_default_data():
    """Link stations are located at points (x, y) and have reach (r) ([x, y, r]):"""
    link_stations = [
        LinkStation(0, 0, 10),
        LinkStation(20, 20, 5),
        LinkStation(10, 0, 12)
    ]
    """points​ (x, y):
(0,0), (100, 100), (15,10) and (18, 18)"""
    devices = [
        Device(0, 0),
        Device(100, 100),
        Device(15, 10),
        Device(18, 18)
    ]

    results = ""
    """get the result of bestt link station"""
    for device in devices:
        results += device.get_best_link_station_with_power(link_stations)

    return results


def main():

    print(run_for_default_data())

if __name__ == "__main__":
    main()
