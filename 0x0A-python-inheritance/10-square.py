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
        """ Calculate square area method """
        return (self.__size ** 2)
