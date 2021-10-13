#!/usr/bin/python3
'''
    Adds a new attribute to an object
    if possible
'''


def add_attribute(obj, atr_name, atr_value):
    '''
    Sets new attribute to obj with name = atr_name
    and value = atr_value if possible,
    otherwise raise TypeError
    '''
    if hasattr(obj, '__dict__'):
        setattr(obj, atr_name, atr_value)
    else:
        raise TypeError("can't add new attribute")
