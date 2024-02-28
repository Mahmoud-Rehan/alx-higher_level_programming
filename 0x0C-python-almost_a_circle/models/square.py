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
