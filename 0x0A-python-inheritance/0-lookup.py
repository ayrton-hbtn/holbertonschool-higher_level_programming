#!/usr/bin/python3
'''
    Returns a list of available attributes
    and methods of object
'''


def lookup(obj):
    '''Takes one parameter (obj)
    '''
    return list(dir(obj))
