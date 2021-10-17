#!/usr/bin/python3
'''
Base class for all other classes
'''


import json


class Base:
    '''
    Creates instance with new id, if id not specified
    it will be the number of instance created at the time
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    '''
    Returns the JSON string representation of list_dictionaries
    '''
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps([element for element in list_dictionaries])

    '''
    Writes the JSON string representation of list_objs to a file
    '''
    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [element.to_dictionary() for element in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_objs))

    '''
    Returns the list of the JSON string representation json_string
    '''
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    '''
    Returns an instance with all attributes already set
    '''
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dup = cls(1, 1)
        elif cls.__name__ == "Square":
            dup = cls(1)
        dup.update(**dictionary)
        return dup

    '''
    Returns a list of instances
    '''
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        s = ""
        try:
            with open(filename, "r") as f:
                list_dict = cls.from_json_string(f.read())
            list_inst = []
            for d in list_dict:
                list_inst.append(cls.create(**d))
            return list_inst
        except FileNotFoundError:
            return []
