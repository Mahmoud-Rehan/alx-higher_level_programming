#!/usr/bin/python3
""" write_file Function Module """


def write_file(filename="", text=""):
    """ Write text to a file function """
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
