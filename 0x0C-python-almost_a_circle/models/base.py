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
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)
