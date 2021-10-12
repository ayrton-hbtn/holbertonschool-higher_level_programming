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
        self.__size = super().integer_validator("size", size)
        super().__init__(self.__size, self.__size)
