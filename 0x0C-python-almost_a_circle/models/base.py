#!/usr/bin/python3
""" Base Class Module """
import json


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Get the json string representation """
        if list_dictionaries is None or not list_dictionaries:
            return ("[]")
        return (json.dumps(list_dictionaries))
