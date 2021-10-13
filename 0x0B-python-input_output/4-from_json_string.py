#!/usr/bin/python3
'''
Returns an object from JSON string
'''


import json


def from_json_string(my_str):
    '''
    from JSON to object
    '''
    return json.loads(my_str)
