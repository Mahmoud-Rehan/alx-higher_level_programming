#!/usr/bin/python3
""" save_to_json_file Function Module """
import json


def save_to_json_file(my_obj, filename):
    """ Writes JSON data in a file function """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dumps(my_obj, f)
