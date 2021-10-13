#!/usr/bin/python3
'''
'''


def add_attribute(obj, atr_name, atr_value):
    '''
    '''
    if type(obj).__module__ == 'builtins':
        raise TypeError("can't add new attribute")
    setattr(obj, atr_name, atr_value)
