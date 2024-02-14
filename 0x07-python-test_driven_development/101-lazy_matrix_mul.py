#!/usr/bin/python3
""" Lazy_matrix_mul Function Module """


from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """ Multiply the matrix function """
    return (matmul(m_a, m_b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
