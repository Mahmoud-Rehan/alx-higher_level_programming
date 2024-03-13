#!/usr/bin/python3
""" Square Class Module """


class Square():
    """ Square Class """
    def __init__(self, size=0):
        """ Initialization method """
        self.__size = size

    def size(self):
        """ Retrieve size method """
        return (self.__size)

    def size(self, value):
        """ Update size method """
        if type(value) is not int:
            raise TypeError("size must be a number")
        if value <= 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate the area method """
        return (self.__size * self.__size)

    def __gt__(self, value):
        """ > Comparison method """
        return (self.__size > value.__size)

    def __lt__(self, value):
        """ < Comparison method """
        return (self.__size < value.__size)

    def __eq__(self, value):
        """ == Comparison method """
        return (self.__size == value.__size)

    def __ne__(self, value):
        """ != Comparison method """
        return (self.__size != value.__size)

    def __ge__(self, value):
        """ >= Comparison method """
        return (self.__size >= value.__size)

    def __le__(self, value):
        """ <= Comparison method """
        return (self.__size <= value.__size)
