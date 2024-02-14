#!/usr/bin/python3
""" Matrix_divided Function Module """


def matrix_divided(matrix, div):
    """ Divides all elements of matrix """
    m = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(m)

    for r in matrix:
        if not isinstance(r, list) or len(r) == 0:
            raise TypeError(m)
        if len(r) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in r:
            if not isinstance(j, (int, float)):
                raise TypeError(m)

    return [[round(j / div, 2) for j in r] for r in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
