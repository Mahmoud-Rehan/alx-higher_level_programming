#!/usr/bin/python3
""" FUNCTION print_square MODULE """


def print_square(size):
    """ FUNCTIN THAT PRINT A SQUARE

    ARGS:
        size: THE LENGTH OF THE SQUARE.

    RAISES:
        TypeError: IF SIZE IS NOT INTEGER.
        ValueError: IF SIZE IS LESS THAN 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for n in range(size):
        print("#" * size + '\n', end="")


if __name__ == "__main__":
    import dotest
    doctest.testfile("tests/4-print_square.txt")
