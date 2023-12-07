#!/usr/bin/python3
""" THE read_file FUNCTION MODULE """


def def read_file(filename=""):
    """ read_file function that reads a file"""
    with open(filename, "r", encoding="utf-8") f:
        print(f.read())
