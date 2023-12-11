#!/usr/bin/python3
""" Rectangle CLASS MODULE """
base = __import__("base.py").Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization function """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
