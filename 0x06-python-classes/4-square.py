#!/usr/bin/python3
""" Square Class Module """


class Square:
    """ Square Class """
    def __init__(self, size=0):
        """ Initialization function """
        self.__size = size

    @property
    def size(self):
        """ Retrive the size function """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Update the value of size function """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Get the area of Square function """
        return (self.__size * self.__size)
