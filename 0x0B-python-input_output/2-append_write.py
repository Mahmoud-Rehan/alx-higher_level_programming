#!/usr/bin/python3
""" append_write FUNCTION MODULE """


def append_write(filename="", text=""):
    """ append_write function """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
