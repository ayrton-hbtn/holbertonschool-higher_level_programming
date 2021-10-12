#!/usr/bin/python3
'''
    Square class, inherits from
    Rectangle
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Constructor with size
    '''
    def __init__(self, size):
        super().__init__(size, size)

    def area(self):
        return super().area()
