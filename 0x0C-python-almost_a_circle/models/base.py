#!/usr/bin/python3
""" Base Class Module """


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization method """
        if id is not None:
            self.id = id
        else:
            id = __nb_objects + 1
