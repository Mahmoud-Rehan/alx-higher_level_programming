#!/usr/bin/python3
""" Add_integer functon module """


def add_integer(a, b=98):
    """ Add two integers function

    Args:
        a (int): First integer
        b (int): Second integer.

    Raises:
        TypeError: If a and b are not integers or floats.

    Returns:
        int: The sum of a and b.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
