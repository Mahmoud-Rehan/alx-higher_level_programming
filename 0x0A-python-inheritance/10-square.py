#!/usr/bin/python3
""" Square CLASS MODULE """
rectangle = __import__("9-rectangle").Rectangle


class Square(rectangle):
    """ Square Class """
    def __init__(self, size):
        """ Instantiation Function """
        self.intger_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ area Function """
        return (self.__size ** 2)
