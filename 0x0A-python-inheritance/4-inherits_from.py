#!/usr/bin/python3
""" inherits_from FUNCTION MODULE """


def inherits_from(obj, a_class):
    """ If the object is an instance of a class that inherited 
    directly or indirectly from the specified class. """

    return (isinstance(obj, a_class) and a_class != type(obj))
