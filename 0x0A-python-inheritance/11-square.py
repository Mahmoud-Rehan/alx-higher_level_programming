#!/usr/bin/python3
""" Square Class Module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ Initialization method """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Calculate the square area method """
        return (self.__size * self.__size)

    def __str__(self):
        """ Return the square description """
        return (f"[Square] {str(self.__size)}/{str(self.__size)}")
