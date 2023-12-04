#!/usr/bin/python3
""" lookup Function Module """


def lookup(obj):
    """ Returns the list of available
    attributes and methods of an object.

    ARGS:
        obj: The object.

    RETURNS:
        list: THe list of methods and attributes.
    """

    return (dir(obj))
