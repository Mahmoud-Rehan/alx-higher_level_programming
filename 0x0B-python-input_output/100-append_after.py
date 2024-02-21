#!/usr/bin/python3
""" append_after Function Module """


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a text in a file
    after a specific string function """
    with open(filename, mode="r", encoding="utf-8") as f1:
        lines = f1.readlines()

    with open(filename, "w") as f2:
        string = ""
        for line in lines:
            string = string + line
            if search_string in line:
                string = string + new_string
        f2.write(string)
