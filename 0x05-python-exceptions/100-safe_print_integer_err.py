#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        n = True
    except Exception as m:
        print("Exception: ", m, file=stderr)
        n = False
    return (n)
