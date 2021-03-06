#!/usr/bin/python3
'''
    Add two numbers, int or float
'''


def add_integer(a, b=98):
    ''' takes two parameters,
        return sum
    '''

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
