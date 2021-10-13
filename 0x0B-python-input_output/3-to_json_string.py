#!/usr/bin/python3
'''
Returns JSON representation of an object
'''


import json


def to_json_string(my_obj):
    '''
    returns JSON
    '''
    return json.dumps(my_obj)
