#!/usr/bin/python3
""" Rectangle CLASS MODULE """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization function """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get width function """
        return (self.__width)

    @width.setter
    def width(self, v):
        """ Set width function """
        self.validate("width", v)
        self.__width = v

    @property
    def height(self):
        """ Get height functin """
        return (self.__height)

    @height.setter
    def height(self, v):
        """ Set height function """
        self.validate("height", v)
        self.__height = v

    @property
    def x(self):
        """ Get x function """
        return (self.__x)

    @x.setter
    def x(self, v):
        """ Set x function """
        self.validate("x", v)
        self.__x = v

    @property
    def y(self):
        """ Get y function """
        return (self.__y)

    @y.setter
    def y(self, v):
        """ Set y function """
        self.validate("y", v)
        self.__y = v

    def validate(self, name, v, check=True):
        """ validate function """
        if type(v) != int:
            raise TypeError("{} must be an integer".format(name))

        if not check and v <= 0:
            raise ValueError("{} must be >= 0".format(name))
        elif check and v < 0:
            raise ValueError("{} must be > 0".format(name))
