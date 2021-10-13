#!/usr/bin/python3
'''
Reads a file and prints its content
to stdout
'''


def read_file(filename=""):
    '''
    Reads file
    '''
    with open(filename) as f:
        for line in f:
            print(line, end="")
