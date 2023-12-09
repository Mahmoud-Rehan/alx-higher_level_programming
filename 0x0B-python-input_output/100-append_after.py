#!/usr/bin/python3
""" append_after FUNCTION MODULE """


def append_after(filename="", search_string="", new_string=""):
    """ append_after function """
    with open(filename, "r", encoding="utf-8") as f:
        lines = []
        while (1):
            line = f.readline()
            if line == "":
                break
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
