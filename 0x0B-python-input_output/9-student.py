#!/usr/bin/python3
""" Student Class Module """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ Initialization method """
        self.first_name = first_name
        self.last-name = last_name
        self.age = age

    def def to_json(self):
        """ Retrieve student's
        dict representation method """
        return (self.__dict__)
