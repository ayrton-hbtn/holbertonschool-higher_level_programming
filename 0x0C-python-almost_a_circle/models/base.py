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
        list_dict = [element.to_dictionary() for element in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dict))

    '''
    Returns the list of the JSON string representation json_string
    '''
    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)
