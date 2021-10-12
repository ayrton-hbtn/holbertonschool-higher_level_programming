#!/usr/bin/python3
'''
    Parent class BaseGeometry
'''


class BaseGeometry:
    '''
    Functionalities
    '''
    def area(self, *args):
        return int(args[0]) * int(args[1])

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value


'''
    Rectangle class, inherits from
    BaseGeometry
'''


class Rectangle(BaseGeometry):
    '''
    Constructor with width & height
    '''
    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def area(self):
        return (super().area(self.__width, self.__height))

    def __str__(self):
        p = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return p


'''
    Square class, inherits from
    Rectangle
'''


class Square(Rectangle):
    '''
    Constructor with size
    '''
    def __init__(self, size):
        super().__init__(size, size)

    def area(self):
        return super().area()
