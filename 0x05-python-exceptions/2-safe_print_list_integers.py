#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    length = 0
    while n < x:
        try:
            print("{:d}".format(my_list[n]), end="")
            length = length + 1
        except (ValueError, TypeError):
            pass
        n = n + 1
    print()
    return (length)
