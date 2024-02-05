#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        n = True
    except Exception as m:
        print("Exception:", m, file=sys.stderr)
        n = False
    return (n)
