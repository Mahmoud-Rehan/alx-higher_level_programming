#!/usr/bin/python3
""" Rectangle CLASS MODULE """
base = __import__("7-base_geometry").BaseGeometry


class Rectangle(base):
    """ Rectangle Class """
    def __init__(self, width, height):
        """ Instantiation Function """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area Function """
        return (self.__height * self.__width)

    def __str__(self):
        """ str Function """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
