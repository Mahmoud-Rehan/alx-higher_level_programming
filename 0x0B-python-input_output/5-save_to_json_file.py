#!/usr/bin/python3
""" save_to_json Function Module """
import json


def save_to_json_file(my_obj, filename):
    """ Save json data in a file function """
    with open(filename, "w", encodnig="utf-8") as f:
        json.dumps(my_obj, f)