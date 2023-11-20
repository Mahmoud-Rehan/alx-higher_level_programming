#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except exception as ex:
        print("Exception: {}", ex, file=sys.stderr)
        return False
