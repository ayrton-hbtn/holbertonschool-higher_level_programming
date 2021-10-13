#!/usr/bin/python3
'''
Appends text to file
'''


def append_write(filename="", text=""):
    '''
    Appends text to file, creates file if
    it doesn't exist
    '''
    with open(filename, "a") as f:
        return f.write(text)
