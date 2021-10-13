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
        self.__size = self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        p = "[{}] ".format(type(self).__name__)
        p += "{}/{}".format(self.__size, self.__size)
        return p
