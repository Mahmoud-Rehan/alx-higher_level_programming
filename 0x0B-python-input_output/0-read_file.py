#!/usr/bin/python3
"""MODULE read_file FUNCTION"""


def read_file(filename=""):
    """read_file function that reads a file"""
    with open(filename, "r", encoding="utf-8") f:
        print(f.read())
