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


    def my_print(self):
        """ Print square method """
        if self.__size == 0:
            print()
            return

        for n in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            print()

    def __str__(self):
        """ Return the string repr of square """
        string = ""
        if self.__size > 0:
            for y in range(self.__position[1]):
                string += '\n'
            for x in range(self.__size):
                string += ' ' * self.__position[0]
                string += '#' * self.__size + '\n'
        return (string[:-1])
