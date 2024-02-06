#!/usr/bin/python3
""" Square Class Module """


class Square:
    """ Square Class """

    def __init__(self, size):
        """ Initialization method

        Args:
            size: Length of the square size.

        Raises:
            TypeError: Size is not int
            ValueError: Size is less than 0

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Area of the Square method

        Returns:
            The square of size.
        """
        return (self.__size ** self.__size)
