#!/usr/bin/python3
"""Class Square Module"""


class Square:

    """Define Class Suare"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def positionself(self, value):
        if (not isinstance(value, tuple) or
            not all(isinstance(n, int) for n in value) or
            not all(n >= 0 for n in value) or
           len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if size == 0:
            print()
        else:
            for i in range(self.__postion[1]):
                print()
            for j in range(self.__size):
                print(" ", self.__position[0], end="")
                print("#", * self.__size, end="")
                print()
