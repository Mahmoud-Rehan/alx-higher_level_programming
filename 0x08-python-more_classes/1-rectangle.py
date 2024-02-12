#!/usr/bin/python3
""" Rectangle Class Module """


class Rectangle:
    """ Rectangle Class """
    def __init__(self, width=0, height=0):
        """ Initializaton method """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ Retrieve width method """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Update width method """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve height method """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Update height method """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
