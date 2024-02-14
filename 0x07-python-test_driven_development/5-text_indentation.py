#!/usr/bin/python3
""" Text_indentation Function Module """


def text_indentation(text):
    """ Indent text function """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".?:":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
