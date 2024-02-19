#!/usr/bin/python3
""" Inherits_from Functon Module """


def inherits_from(obj, a_class):
    """ Checks if object is an instance of class
    directly or indirectly """
    return (isinstance(obj, a_class) adn type(obj) is not a_class)
