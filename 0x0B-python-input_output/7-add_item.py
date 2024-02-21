#!/usr/bin/python3
"""Module that loads, adds and saves arguments to a Python list"""
from sys import argv


load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

my_list = list(argv[1:])

try:
    json_data = load('add_item.json')
except Exception:
    json_data = []

json_data.extend(my_list)
save(json_data, 'add_item.json')
