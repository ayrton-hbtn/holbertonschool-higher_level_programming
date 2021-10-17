#!/usr/bin/python3
'''
Class Rectangle, inherits from Class Base
'''


from models.base import Base


class Rectangle(Base):
    '''
    Constructor with private attributes width, height, x and y.
    id assigned with Base constructor logic
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        self.id = id
        super().__init__(self.id)

    '''
    Getter for each attribute
    '''
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    '''
    Setter for each attribute
    '''
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    '''
    Public method area()
    returns area of Rectangle object
    '''
    def area(self):
        return self.__width * self.__height

    '''
    Public method display()
    prints a Recrangle object made of #
    '''
    def display(self):
        for line in range(self.__y):
            print()
        for row in range(self.__height):
            for space in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print('#', end="")
            print()

    '''
    Override __str__ method
    '''
    def __str__(self):
        p = f"[{type(self).__name__}] ({self.id}) "
        p += f"{self.__x}/{self.__y} - {self.__width}/{self.__height}"
        return p

    '''
    Assigns an argument to each attribute of instance
    no-keyword arguments
    '''
    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except:
                pass
        else:
            for attr, val in kwargs.items():
                if attr == "width":
                    self.__width = val
                elif attr == "height":
                    self.__height = val
                elif attr == "x":
                    self.__x = val
                elif attr == "y":
                    self.__y = val
                elif attr == "id":
                    self.id = val
                else:
                    raise KeyError(f"{attr} is not an attribute of {type(self).__name__}")
