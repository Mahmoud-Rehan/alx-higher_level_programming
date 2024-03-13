#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value


    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
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
        return (size ** 2)

    