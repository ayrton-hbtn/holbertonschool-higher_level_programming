#!/usr/bin/python3
'''
MyInt class inherits from int
'''


class MyInt(int):
    '''
    Works the same of int, but operators
    == and != are inverted
    '''
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
