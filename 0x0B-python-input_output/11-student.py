#!/usr/bin/python3
'''
Class Student
'''


class Student:
    '''
    Instatiation with first_name,
    last_name and age
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            d = {}
            for i in attrs:
                try:
                    d[i] = getattr(self, i)
                except Exception:
                    pass
            return d
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key in json.keys():
            setattr(self, key, json[key])
