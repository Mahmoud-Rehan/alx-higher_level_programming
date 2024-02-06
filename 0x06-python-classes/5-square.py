#!/usr/bin/python3
""" Square Class Module """


class Square:
    """ Square Class """
    def __init__(self, size=0):
        """ Initialization function """
        self.__size = size

    @property
    def size(self):
        """ Retrieve the size function """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Update the size value function """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Get the area of a Square function """
        return (self.__size * self.__size)

    def my_print(self):
        """ Print the Square function """
        if not self.__size == 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()
