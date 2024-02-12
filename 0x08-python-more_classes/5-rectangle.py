#!/usr/bin/python3
""" Rectangle Class Method """


class Rectangle:
    """ Rectangle Class """
    def __init__(self, width=0, height=0):
        """ Initialization method """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieve the width value method """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Update the width value method """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve height method """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Update height value method """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculate the area of rectangle method """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Calculate the perimeter of rectangle method """
        if not self.__width == 0 and not self.__height == 0:
            return (2 * (self.__width + self.__height))
        else:
            return (0)

    def __str__(self):
        """ Format string method """
        string = ""
        if self.__width != 0 and self.__height != 0:
            for r in range(self.__height):
                for c in range(self.__width):
                    string += "#"
                if r != (self.__height - 1):
                    string += "\n"

        return (string)

    def __repr__(self):
        """ Format string representation method """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """ Print message after an instance is deleted method """
        print("Bye rectangle...")
