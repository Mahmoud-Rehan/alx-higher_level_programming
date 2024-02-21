#!/usr/bin/python3
""" load_from_json_file Function Module """
import json


def load_from_json_file(filename):
    """ Load json data from file function """
    with open(filename, mode="w", encoding="utf-8") as f:
        return (json.load(f))
