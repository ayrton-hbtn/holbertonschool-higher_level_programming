#!/usr/bin/python3
'''
    Checks if obj is or inherits from a_class
'''


def is_kind_of_class(obj, a_class):
    '''
    Returns True if obj inherits from a_class,
    False otherwise
    '''
    return isinstance(obj, a_class)
