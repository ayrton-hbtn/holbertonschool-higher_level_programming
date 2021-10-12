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
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        p = "[{}] ".format(type(self).__name__)
        p += "{}/{}".format(self.__width, self.__height)
        return p
