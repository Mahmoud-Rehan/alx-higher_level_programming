#!/usr/bin/python3
""" append_write Function Module """


def append_write(filename="", text=""):
    """ Append text to a file function """
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
