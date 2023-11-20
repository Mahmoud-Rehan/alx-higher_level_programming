#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    x = True
    try:
        print("{:d}".format(value))
    except Exception as ex:
        print("Exception:", ex, file=sys.stderr)
        x = False
    return x
