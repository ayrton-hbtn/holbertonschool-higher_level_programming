#!/usr/bin/python3
'''
Converts dictionary description with simple data
structures for JSON
'''


def class_to_json(obj):
    '''
    Returns dictionary obj
    for JSON serialization
    '''
    return obj.__dict__
