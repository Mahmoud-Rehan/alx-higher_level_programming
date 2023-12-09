#!/usr/bin/python3
""" pascal_triangle FUNCTION MODULE """

def pascal_triangle(n):
    """ pascal_triangle function """
    if n <= 0:
        return ([])

    tris = [[1]]
    while len(tris) != n:
        triangle = tris[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append(1)
        tris.append(temp)
    return (tris)
