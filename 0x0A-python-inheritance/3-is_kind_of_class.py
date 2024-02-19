#!/usr/bin/python3
""" Is_kind_of_class Function Module """


def is_kind_of_class(obj, a_class):
    """ Checks if obj is an instance of class """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
