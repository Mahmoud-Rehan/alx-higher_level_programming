#!/usr/bin/python3

class Student:
    """ initialization function """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json function """
        try:
            for a in attrs:
                if type(a) is not str:
                    return (self.__dict__)
        except Exception:
            return (self.__dict__)

        dictionary = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                ictionary[k] = v
        return (dictionary)

    def reload_from_json(self, json):
        """ reload_from_json function """
        for k, v in json.items():
            if k in self.__dict__:
                self.__dict__[k] = v
