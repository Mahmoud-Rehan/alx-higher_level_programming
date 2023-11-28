#!/usr/bin/python3
""" FUNCTION say_my_name MODULE """


def say_my_name(first_name, last_name=""):
    """ FUNCTION THAT PRINT FIRST AND LAST NAME

    ARGS:
        first_name: THE FIRST NAME STRING.
        last_name: THE LAST NAME STRING.

    RAISES:
        TypeError: IF FIRST NAME OR LAST NAME NOT STRING.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))


if __name__ == "-_main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
