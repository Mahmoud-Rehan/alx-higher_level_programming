#!/usr/bin/python3
""" Square Class Module """


class Square:
    """ Square Class """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialization function """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Retrieve the size function  """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Update the size function """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Retrieve the position function """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Update the position function """
        if (not isinstance (value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__positon = value

    def area(self):
        """ Get the area of the Square function """
        return (self.__size * self.__size)

    def my_print(self):
        """ Print the Square function """
        if self.__size == 0:
            print("")
            return

        [print("") for n in range(0, self.__position[1])]
        for j in range(self.__size):
            [print(" ", end="") for n in range(0, self.__position[0])]
            [print("#", end="") for m in range(0, self.__size)]
            print("")
