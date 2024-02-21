#!/usr/bin/python3
""" Student Class Module """


class Student:
    """ Student Class """
    def __init__(self, first_name, last_name, age):
        """ Initialization method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves the dict representation of a Student method """
        if attrs is None:
            return (self.__dict__)

        my_dict = dict()
        for item in attrs:
            try:
                my_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return (my_dict)
