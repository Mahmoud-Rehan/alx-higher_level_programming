#!/usr/bin/python3
""" read_file Function Module """


def read_file(filename=""):
    """ Read the text of the file function """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
