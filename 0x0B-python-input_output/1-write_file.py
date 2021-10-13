#!/usr/bin/python3
'''
Writes text into file
'''


def write_file(filename="", text=""):
    '''
    Writes text into file, creates file
    if it doesn't exist
    '''
    with open(filename, "w") as f:
        return f.write(text)
