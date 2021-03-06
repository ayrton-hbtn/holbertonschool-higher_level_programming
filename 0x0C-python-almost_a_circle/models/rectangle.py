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
    width getter
    '''
    @property
    def width(self):
        return self.__width

    '''
    height getter
    '''
    @property
    def height(self):
        return self.__height

    '''
    x getter
    '''
    @property
    def x(self):
        return self.__x

    '''
    y getter
    '''
    @property
    def y(self):
        return self.__y

    '''
    width setter
    '''
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    '''
    height setter
    '''
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    '''
    x setter
    '''
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    '''
    y setter
    '''
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
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
    Update instance attributes using args and kwargs
    (no-keyword vs keyword arguments)
    '''
    def update(self, *args, **kwargs):
        li = len(args)
        if li > 0:
            setattr(self, "id", args[0])
        if li > 1:
            setattr(self, "width", args[1])
        if li > 2:
            setattr(self, "height", args[2])
        if li > 3:
            setattr(self, "x", args[3])
        if li > 4:
            setattr(self, "y", args[4])
        for key, val in kwargs.items():
            setattr(self, key, val)

    '''
    Returns the dictionary representation of a Rectangle
    '''
    def to_dictionary(self):
        obj = {}
        obj['id'] = self.id
        obj['width'] = self.__width
        obj['height'] = self.height
        obj['x'] = self.__x
        obj['y'] = self.__y
        return obj
