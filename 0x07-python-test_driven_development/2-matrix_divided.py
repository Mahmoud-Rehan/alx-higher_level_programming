#!/usr/bin/python3
""" FUNCTION matrix_divided MODULE """


def matrix_divided(matrix, div):
    """
    DIVIDES ALL ELEMENTS OF A MATRIX.

    ARGS:
        matrix: LIST OF LISTS OF INTEGER OR FLOAT VALUES.
        div: NUMBER INTEGER OR FLOAT VALUE.

    RAISES:
        TypeError: if matrix is not list of lists contains INT or FLOAT.
        TypeError: if each row of matrix not the same size.
        TypeError: if div not int or float values.
        ZeroDivisionError: if div is zero.

    RETURNS:
        list: new matrix.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    for r in matrix:
        if not isinstance(r, list) or len(r) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        if len(r) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for n in r:
            if not isinstance(n, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")

    return [[round(n / div, 2) for n in r] for r in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
