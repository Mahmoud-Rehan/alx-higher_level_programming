#!/usr/bin/python3
""" Rectangle CLASS MODULE """
from model.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization function """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get width function """
        return (self.__width)

    @width.setter
    """ Set width function """
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """ Get height functin """
        return (self.__height)

    @height.setter
    def height(self, height):
        """ Set height function """
        self.__height = height

    @property
    def x(self):
        """ Get x function """
        return (self.__x)

    @setter.x
    def x(self, x):
        """ Set x function """
        self.__x = x

    @property
    def y(self):
        """ Get y function """
        return (self.__y)

    @y.setter
    def y(self, y):
        """ Set y function """
        self.__y = y
