#!/usr/bin/python3
""" Square Class Module """

class Square:
    """ Square Class """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialization Method """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Retrieve the size method """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Update the size method """
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value


    @property
    def position(self):
        """ Retrieve the position method """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Update the position method """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")

        self.__position = value

    def area(self):
        """ Calculate the area method """
        return (size ** 2)
