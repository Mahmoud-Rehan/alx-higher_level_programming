#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return (None)
    for row in matrix:
        if len(row) == 0:
            print()
        for n in range(len(row)):
            print("{:d}".format(row[n]), end="\n"
                  if n is len(row) - 1 else " ")
