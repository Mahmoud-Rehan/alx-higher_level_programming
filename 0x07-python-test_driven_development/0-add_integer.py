#!/usr/bin/python3


def add_integer(a, b=98):
    """ Add two integers function """
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
