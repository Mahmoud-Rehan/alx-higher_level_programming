#!/usr/bin/python3
""" Base CLASS MODULE """
import json
import csv


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string function """
        if list_dictionaries is None:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file function """
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string function """
        if json_string is None:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ creat instance function """
        from models.square import Square
        from models.rectangle import Rectangle
        if cls is Rectangle:
            instance = Rectangle(1, 1)
        elif cls is Square:
            instance = Square(1)
        else:
            instance = None
        instance.update(**dictionary)
        return (instance)

    @classmethod
    def load_from_file(cls):
        """ load_from_file function """
        from os import path
        filename = "{}.json".format(cls.__name__)
        if not path.isfile(filename):
            return ([])
        with open(filename, "r", encoding="utf-8") as f:
            return ([cls.create(**dicts)
                    for dicts in cls.from_json_string(f.read())])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save_to_file_csv function """
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                             for obj in list_objs]
            else:
                list_objs = [[obj.id, obj.size, obj.x, obj.y]
                             for obj in list_objs]

        with open("{}.csv".format(cls.__name__), "w",
                  newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """ load_-from_csv_file function """
        from models.rectangle import Rectangle
        from models.square import Square
        new_list = []
        with open("{}.csv".format(cls.__name__), "r",
                  newline="", encoding="utf-8") as f:
            r = csv.reader(f)
            for line in r:
                line = [int(item) for item in line]
                if cls is Rectangle:
                    dictionary = {"id": line[0], "width": line[1], "height":
                                  line[2], "x": line[3], "y": line[4]}
                else:
                    dictionary = {"id": line[0], "size": line[1],
                                  "x": line[2], "y": line[3]}
                new_list.append(cls.create(**dictionary))
        return (new_list)
