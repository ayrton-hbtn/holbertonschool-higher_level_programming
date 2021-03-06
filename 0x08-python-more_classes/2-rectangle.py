#!/usr/bin/python3

'''Define Rectangle object
'''


class Rectangle:
    '''Constructor method with width and height
    '''
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    ''' width getter '''
    @property
    def width(self):
        return self.__width

    ''' height getter '''
    @property
    def height(self):
        return self.__height

    ''' width setter '''
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    ''' height setter '''
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    ''' calculates area of rectangle object '''
    def area(self):
        return self.__width * self.__height

    ''' calculates perimeter of rectangle object '''
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
