#!/usr/bin/python3
""" Rectangle CLASS MODULE """
rectangle = __import__('9-rectangle').Rectangle


class Square(rectangle):
    """ Square Class """
    def __init__(self, size):
        """ Instantiation Function """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area Fuction """
        return (self.__size ** 2)

    def __str__(self):
        """ str Function """
        return ("[Square] {}/{}".format(str(self.__size), str(self.__size)))
