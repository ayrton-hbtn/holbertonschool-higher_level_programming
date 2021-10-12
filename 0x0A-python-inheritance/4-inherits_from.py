#!/usr/bin/python3
'''
    Checks if obj inherited from a_class
'''


def inherits_from(obj, a_class):
    '''
    Returns True if obj inherited (but not is)
    from a_class, False otherwise
    '''
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
