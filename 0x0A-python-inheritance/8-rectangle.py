#!/usr/bin/python3
'''
    Rectangle class, inherits from
    BaseGeometry
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Constructor with width & height
    '''
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
