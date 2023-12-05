#!/usr/bin/python3
""" MyList Class Module """


class MyList(list):
    """ MyList Class """
    def print_sorted(self):
        """ Prints a sorted list """
        print(sorted(self))
