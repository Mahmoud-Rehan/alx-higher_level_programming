#!/usr/bin/python3
""" MyInt CLASS MODULE """


class MyInt(int):
    """ The class MyInt """
    def __new__(cls, *args, **kwargs):
        """ Integer repl version """
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __ne__(self, num):
        """ set != to be == """
        return (int(self) == num)

    def __eq__(self, num):
        """ set == to be != """
        return (int(self) != num)
