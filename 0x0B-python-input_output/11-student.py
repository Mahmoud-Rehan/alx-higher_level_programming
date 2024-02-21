#!/usr/bin/python3
"""Student Class Module """


class Student:
    """ Student Class """
    def __init__(self, first_name, last_name, age):
        """ Initalization method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves student's dict representation method """
        if attrs is None:
            return (self.__dict__)

        my_dict = dict()
        for item in attrs:
            try:
                myw_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return (my_dict)

    def reload_from_json(self, json):
        """ Replaces all Students attributes method """
        self.__dict__.update(json)
