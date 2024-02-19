#!/usr/bin/python3
""" MyInt Class Module """


class MyInt(int):
    """ Myint Class """
    def __new__(cls, *args, **kwargs):
        """Creates a new instance of the integer class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __ne__(self, other):
        """ Converts != to == """
        return (int(self) == other)

    def __eq__(self, other):
        """ Converts == to != """
        return (int(self) != other)
