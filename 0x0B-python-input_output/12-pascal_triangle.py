#!/usr/bin/python3
""" pascal_triangle method """


def pascal_triangle(n):
    """ Create pascal triangle method """
    if n <= 0:
        return ([])
    if n == 1:
        return ([[1]])

    triangle = [[1]]

    for k in range(n - 1):
        triangle.append([x + n for x, n in zip(triangle[-1] + [0],
                                             [0] + triangle[-1])])
    return (triangle)
