#!/usr/bin/python3
""" Square Class Module """


class Square:
    """ Square Class """
    def __init__(self, size):
        """ Initialization method """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Area of the Square method """
        return (self.__size ** 2)
