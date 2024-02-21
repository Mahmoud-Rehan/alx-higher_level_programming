#!/usr/bin/python3
""" read_file Function Module """


def read_file(filename=""):
    """ Read the text of the file function """
    with open(filename, encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
