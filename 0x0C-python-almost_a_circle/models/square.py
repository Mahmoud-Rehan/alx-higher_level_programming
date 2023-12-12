#!/usr/bin/python3
""" Square CLASS MODULE """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization function """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str function """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.height))

    @property
    def size(self):
        """ Get size function """
        return (self.height)

    @size.setter
    def size(self, v):
        """ Set size function """
        self.width = v
        self.height = v

    def update(self, *args, **kwargs):
        """ update value function """
        if args and len(args) != 0:
            length = 0
            for a in args:
                if length == 0:
                    if a is None:
                        break
                    else:
                        self.id = a
                elif length == 1:
                    self.size = a  
                elif length == 2:
                    self.x = a
                elif length == 3:
                    self.y = a
                length = length + 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        break
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
