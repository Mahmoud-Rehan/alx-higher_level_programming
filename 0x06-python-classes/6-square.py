#!/usr/bin/python3
""" Square Class Module """


class Square:
    """ Square Class """
    def __init__(self, size=0, position=(0, 0)):
        """Initialiation function """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of a square function"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Update the size function"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the Square function"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Update position functon """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Get the area of Square function """
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square function"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                for m in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * self.__size)
