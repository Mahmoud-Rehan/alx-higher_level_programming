#!/usr/bin/python3
""" Multiplication of two Matrices and
return the result Matrix Function Module """


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    if type(m_) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for a_row in m_a:
        if type(a_row) is not list:
            raise TypeError("m_a must be a list of lists")

    for b_row in m_b:
        if type(b_row) is not list:
            raise TypeError("m_b must be a list of lists")

    for a_row in m_a:
        for a_element in a_row:
            if not isinstance(a_element, int)
            and not isinstance(a_element, float):
                raise TypeError("m_a should contain only integers or floats")

    for b_row in m_b:
        for b_element in b_row:
            if not isinstance(b_element, int)
            and not isinstance(b_element, float):
                raise TypeError("m_b should contain only integers or floats")

    if not all(len(a_row) == len(m_a[0]) for a_row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(b_row) == len(m_b[0]) for b_row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    a = 0

    for col in m_a[0]:
        a += 1

    b = 0

    for row in m_b:
        b += 1

    if a != b:
        raise ValueError("m_a and m_b can't be multiplied")

    matrix = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]

    for n in range(len(m_a)):
        for m in range(len(m_b[0])):
            for r in range(len(m_b)):
                matrix[n][m] += m_a[n][r] * m_b[r][m]

    return (matrix)
