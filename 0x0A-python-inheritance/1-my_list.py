#!/usr/bin/python3
'''
    Inherits from list class, prints list object
'''


class MyList(list):
    '''Prints list object, sorted
    '''
    def print_sorted(self):
        print(sorted(self))
