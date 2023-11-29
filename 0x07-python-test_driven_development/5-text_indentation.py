#!/usr/bin/python3
""" FUNCTION test_indentation MODULE """


def text_indentation(text):
    """ FUNCTION THAT PRINTS 2 LINES
    AFTER ., ?, : CHARACTERS.

    ARGS:
        test: STRING.

    RAISES:
        TypeError: IF tEXT IS NOT A STRING.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for s in ":?.":
        text = (s + '\n\n').join([n.strip(" ") for n in text.split(s)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
