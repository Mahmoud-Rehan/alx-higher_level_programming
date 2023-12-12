#!/usr/bin/python3
""" Square CLASS MODULE """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization function """
        super().__init__(id, x, y, size, size)

    def __str__(self):
        """ str function """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.height))
