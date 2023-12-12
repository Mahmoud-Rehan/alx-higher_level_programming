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
        self.validate("width", v, False)
        self.__width = v

    @property
    def height(self):
        """ Get height functin """
        return (self.__height)

    @height.setter
    def height(self, v):
        """ Set height function """
        self.validate("height", v, False)
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
        if not isinstance(v, int):
            raise TypeError("{} must be an integer".format(name))
        if check and v < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not check and v <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ area function """
        return (self.width * self.height)

    def display(self):
        """ The display function """
        p = "\n" * self.y + \
            (" " * self.x + "#" * self.width + "\n") * self.height
        print(p, end="")

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    def update(self, *args, **kwargs):
        """ update the values function """
        if args and len(args) != 0:
            length = 0
            for a in args:
                if length == 0:
                    if a is None:
                        break
                    else:
                        self.id = a
                elif length == 1:
                    self.width = a
                elif length == 2:
                    self.height = a
                elif length == 3:
                    self.x = a
                elif length == 4:
                    self.y = a
                length = length + 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        break
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
