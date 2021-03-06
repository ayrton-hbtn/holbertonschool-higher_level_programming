#!/usr/bin/python3

'''Define Rectangle object
'''


class Rectangle:
    '''Constructor method with width and height
    '''

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    ''' make object readable and printable,
        generates output for user
    '''
    def __str__(self):
        p = ''
        if self.__width == 0 or self.__height == 0:
            return p
        for line in range(self.__height):
            for col in range(self.__width):
                p += str(self.print_symbol)
            p += '\n'
        return p[:-1]

    ''' makes object readable for developers '''
    def __repr__(self):
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    ''' deletes object and prints a message '''
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    ''' static method to compare rectangles,
        returns biggest based on area
    '''
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
