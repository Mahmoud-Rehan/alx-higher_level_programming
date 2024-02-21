#!/usr/bin/python3
""" from_json_string Function Module """
import json


def from_json_string(my_str):
    """ Deserialize strings Function """
    return (json.load(my_str))
