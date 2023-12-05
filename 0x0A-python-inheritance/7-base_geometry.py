#!/usr/bin/python3
""" BaseGeometry CLASS MODULE """


class BaseGeometry:
    """ BaseGeometry Class """
    def area(self):
        """ area Function """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator Function """
        if int != type(value):
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
