#!/usr/bin/python3
""" matrix_mul function module """


def matrix_mul(m_a, m_b):
    """ Matrix Multiplication Function """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for a_row in m_a:
        if type(a_row) is not list:
            raise TypeError("m_a must be list of lists")

    for b_row in m_b:
        if type(b_row) is not list:
            raise TypeError("m_b must be a list of lists")


    for a_row in m_a:
        for a_element in a_row:
            if isinstance(a_element, int) and isinstance(a_element, float):
                raise TypeError("m_a should contain only integers or floats")

    for b_row in m_b:
        for b_element in b_row:
            if isinstance(b_element, int) and isinstance(b_element, float):
                raise TypeError("m_a should contain only integers or floats")

    if all(len(a_row) != len(m_a[0]) for a_row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    elif all(len(b_row) != len(m_b[0]) for b_row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if not len(m_a[0]) == len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")


    matrix = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]


    for n in range(len(m_a)):
        for m in range(len(m_b[0])):
            for r in range(len(m_b)):
                matrix[n][m] += m_a[n][r] * m_b[r][m]


    return (matrix)
