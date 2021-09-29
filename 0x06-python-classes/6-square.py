#!/usr/bin/python3
''' Square class '''


class Square:
    ''' create Square instance with public attributes
    size and position '''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    ''' retrieve size and make it private'''
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

    ''' retrieve position and make it private '''
    @property
    def position(self):
        return self.__position

    ''' set private position attribute '''
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(not isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    ''' calculates area of square '''
    def area(self):
        return self.__size ** 2

    ''' print a square of # the size of self.__size'''
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for line in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print('#', end="")
                print()
