#!/usr/bin/python3
'''
    Checks if obj is exactly an instance
    of a_class
'''


def is_same_class(obj, a_class):
    '''
    Returns True if obj is of type a_class,
    False otherwise
    '''
    return type(obj) is a_class
