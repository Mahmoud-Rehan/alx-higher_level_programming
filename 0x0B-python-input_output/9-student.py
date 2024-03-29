#!/usr/bin/python3
""" Student Class Module """


class Student:
    """ Student Class """
    def __init__(self, first_name, last_name, age):
        """ Initialization method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a student's dictionary representation """
        return (self.__dict__)
