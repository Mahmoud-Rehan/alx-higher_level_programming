#!/usr/bin/python3
""" MyList Cass Module """


class MyList(list):
    """ MyList Class """
    def print_sorted(self):
        """ Print sorted list method """
        print(sorted(self))
