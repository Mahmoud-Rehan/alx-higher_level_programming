#!/usr/bin/python3
""" add_atributte FUNCTION MODULE """


def add_attribute(ob, name, value):
    """ Adds a new atributte to an object """

    if not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(ob, name, value)
