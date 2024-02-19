#!/usr/bin/python3
""" BaseGeometry Class Module """


class BaseGeometry:
    """ BaseGeometry Class """
    def area(self):
        """ Not implemented area method """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Check if value is integer method """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
