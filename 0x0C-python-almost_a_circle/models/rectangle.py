#!/usr/bin/python3
""" Rectangle Class Method """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization method """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Retrieve the value of width method """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Update the value of width method """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve the value of height method """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Update the value of height method """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Retrieve the value of x method """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ Update the value of x method """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Retrieve the value of y method """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ Update the value of y method """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate the area method """
        return (self.width * self.height)

    def display(self):
        """ Print the rectangle method """
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ View rectangle info """
        return ("[Rectangle] ({id}) {x}/{y} - {width}/{height}"
                .format(id=self.id, x=self.x, y=self.y,
                        width=self.width, height=self.height))
