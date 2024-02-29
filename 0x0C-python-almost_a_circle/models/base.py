#!/usr/bin/python3
""" Base Class Module """
import json
import csv
import os.path
import turtle


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Get the json string representation """
        if list_dictionaries is None or not list_dictionaries:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes json string representation to a file """
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        filename = ("{}.json".format(cls.__name__))
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ Get the list of json string representation """
        if json_string is None or not json_string:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ Set all instances of an attribute method """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """ Gets a list of instances method """
        filename = "{}.json".format(cls.__name__)
        if os.path.exists(filename) is False:
            return ([])
        with open(filename, "r", encoding="utf-8") as f:
            return ([cls.create(**dictionary) for dictionary in
                     cls.from_json_string(f.read())])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serialize in CSV file method """
        from models.square import Square
        from models.rectangle import Rectangle
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="") as f:
            w = csv.writer(f)
            if cls is Rectangle:
                for i in list_objs:
                    w.writerow([i.id, i.width, i.height, i.x, i.y])
            if cls is Square:
                for j in list_objs:
                    w.writerow([j.id, j.size, j.x, j.y])

    @classmethod
    def load_from_file_csv(cls):
        """ Deserialize in CSV file method """
        from models.square import Square
        from models.rectangle import Rectangle
        filename = "{}.csv".format(cls.__name__)
        objects = list()
        with open(filename, "r", encoding="utf-8", newline="") as f:
            r = csv.reader(f)
            for line in r:
                line = [int(n) for n in line]
                if cls is Rectangle:
                    dictionary = {"id": line[0], "width": line[1],
                                  "height": line[2], "x": line[3],
                                  "y": line[4]}
                else:
                    dictionary = {"id": line[0], "size": line[1],
                                  "x": line[2], "y": line[3]}
                objects.append(cls.create(**dictionary))
        return (objects)

    @staticmethod
    def draw(list_rectangles, list_squares):
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for n in list_rectangles + list_squares:
            screen = turtle.Turtle()
            screen.color((randrange(255), randrange(255), randrange(255)))
            screen.pensize(1)
            screen.penup()
            screen.pendown()
            screen.setpos((n.x + screen.pos()[0], n.y - screen.pos()[1]))
            screen.pensize(10)
            screent.forward(n.width)
            screen.left(90)
            screen.forward(n.height)
            screenscreen.left(90)
            screen.forward(n.width)
            screen.left(90)
            screen.forward(n.height)
            screen.left(90)
            screen.end_fill()

        time.sleep(5)
