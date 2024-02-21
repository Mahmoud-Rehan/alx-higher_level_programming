#!/usr/bin/python3
""" read_file Function Module """


def read_file(filename=""):
    """ Reads data from a file function """
    with open(filename, mode="r", encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
