#!/usr/bin/python3
""" Rectangle Class Module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization method """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Retrieve the value of width """
        return (self.__x)

    @width.setter
    def width(self, value):
        """ Update the value of width """
        self.check_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """ Retrieve the value of height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Update the value of height """
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """ Retrieve the value of x """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Update the value of x """
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """ Retrieve the value of y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Update the value of y method """
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, equal=True):
        """ Validation method """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if equal and value < 0:
            raise ValueError(f"{name} must be >= 0")
        elif not equal and value <= 0:
            raise ValueError(f"{name} must be > 0")
