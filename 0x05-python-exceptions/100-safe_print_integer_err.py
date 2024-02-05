#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    n = True
    try:
        print("{:d}".format(value))
    except Exception as m:
        print("Exception: ", m, file=stderr)
        n = False
    return (n)
