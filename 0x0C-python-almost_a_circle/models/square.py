#!/usr/bin/python3
""" Square Class Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Class string representation """
        return ("[Square] ({id}) {x}/{y} - {size}"
                .format(id=self.id, x=self.x, y=self.y, size=self.width))

    @property
    def size(self):
        """ Retrieve the value of size method """
        return (self.width)

    @size.setter
    def size(self, value):
        """ Update the size value method """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update the class square values """
        if args is not None and len(args) != 0:
            my_list = ["id", "size", "x", "y"]
            i = 0
            for arg in args:
                if my_list[i] == "size":
                    setattr(self, "height", arg)
                    setattr(self, "width", arg)
                else:
                    setattr(self, my_list[i], arg)
                i = i + 1
        else:
            for k, v in kwargs.items():
                if k == "size":
                    setattr(self, "height", v)
                    setattr(self, "width", v)
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """ View the dict representation of square method """
        return ({"id": self.id,
                 "size": self.size,
                 "x": self.x,
                 "y": self.y})
