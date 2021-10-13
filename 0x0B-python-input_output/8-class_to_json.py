#!/usr/bin/python3
'''
Converts dictionary description with simple data
structures for JSON
'''


import json


def class_to_json(obj):
    '''
    Returns JSON serialization of
    object as dictionary
    '''
    s = json.dumps(obj.__dict__)
    return json.loads(s)
