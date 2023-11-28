#!/usr/bin/python3
""" ADD_INTEGER FUNCTION MODULE """


def add_integer(a, b=98):
    """
    ADD TWO INTEGER VALUES

    ARGS:
        a: FIRST INTEGER.
        b: SECOND INTEGER WTIH DEFAULT VALUE 98.

    RAISES:
        TypeError: IF a OR b ARE NOT INTEGERS OR FLOAT VALUES.

    RETURNS:
        THE SUM OF a AND b.
    """

    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

if __name__ == "__main__":
    import doctest
    doctest.testmode("tests/0-add_integer.txt")
