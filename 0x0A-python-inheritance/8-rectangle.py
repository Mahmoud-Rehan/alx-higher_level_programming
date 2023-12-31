#!/usr/bin/python3
""" Rectangle CLASS MODULE """
base = __import__("7-base_geometry").BaseGeometry


class Rectangle(base):
    """ Class Rectangle """
    def __init__(self, width, height):
        """ Initialization function """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
