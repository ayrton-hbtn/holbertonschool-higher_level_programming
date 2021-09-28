#!/usr/bin/python3
''' Square class '''


class Square:
    ''' create Square instance with private size attribute'''
    def __init__(self, size=0):
        self.size = size

    ''' retrieve size '''
    @property
    def size(self):
        return self.__size

    ''' set private size attribute '''
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    ''' calculates area of square '''
    def area(self):
        return self.__size ** 2
