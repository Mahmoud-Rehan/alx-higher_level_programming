#!/usr/bin/python3
""" MyInt CLASS MODULE """


class MyInt(int):
    """ MyInt Class """
    def __new__(cls, *args, **kwargs):
        """ Integer repl version """
        return super(MyInt, cls).__new__(cls, *args, **args)

    def __ne__(self, num):
        """ set != to be == """
        return (int(self) == num)

    def __eq__(self, num):
        """ set == to be != """
        return (int(self) != num)
