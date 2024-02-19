#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(o, attribute, value):
    """ Add a new attribute to an object """
    if not hasattr(o, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(o, attribute, value)
