#!/usr/bin/python3
""" MagicClass Class Module """
import math


class MagicClass:
    """ MagicClass Class """
    def __init__(self, radius=0):
        """ Initialization Method """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Calculate the area method """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ Calculate the circumference method """
        return (2 * math.pi * self.__radius)
