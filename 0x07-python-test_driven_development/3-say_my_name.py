#!/usr/bin/python3
'''
    Takes one string argument, optionally two
'''


def say_my_name(first_name, last_name=""):
    '''prints the text "my name is"
    followed by first and last name.
    arguments must be string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
