#!/usr/bin/python3
'''
Square Class, Inherits from Rectangle.
'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Constructor with private attributes size, x & y.
    id assigned with same logic as parent class
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    '''
    Getter for size attribute
    '''
    @property
    def size(self):
        return super().width

    '''
    Setter for size attribute, inherits validation
    from parent class
    '''
    @size.setter
    def size(self, value):
        super(Square, type(self)).width.fset(self, value)

    '''
    Override __str__ method
    '''
    def __str__(self):
        p = f"[{type(self).__name__}] ({self.id}) "
        p += f"{self.x}/{self.y} - {self.size}"
        return p

    '''
    Update instance attributes using args and kwargs
    '''
    def update(self, *args, **kwargs):
        li = len(args)
        if li > 0:
            setattr(self, "id", args[0])
        if li > 1:
            setattr(self, "size", args[1])
        if li > 2:
            setattr(self, "x", args[2])
        if li > 3:
            setattr(self, "y", args[3])
        for key, val in kwargs.items():
            setattr(self, key, val)

    '''
    Returns the dictionary representation of a Square
    '''
    def to_dictionary(self):
        obj = {}
        obj['id'] = self.id
        obj['size'] = self.width
        obj['x'] = self.x
        obj['y'] = self.y
        return (obj)