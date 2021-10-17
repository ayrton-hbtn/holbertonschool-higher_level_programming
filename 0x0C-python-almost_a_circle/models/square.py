#!/usr/bin/python3
'''
Square Class, Inherits from Rectangle.
'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Constructor with private attributes size, x & y,
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
        p += f"{self.x}/{self.y} - {self.width}"
        return p

    '''
    Update instance attributes using args and kwargs
    '''
    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception:
                pass
        else:
            for attr, val in kwargs.items():
                if attr == "size":
                    self.width = val
                elif attr == "x":
                    self.x = val
                elif attr == "y":
                    self.y = val
                elif attr == "id":
                    self.id = val
                else:
                    raise KeyError(f"{attr}: attribute not found")

    '''
    Returns the dictionary representation of a Square
    '''
    def to_dictionary(self):
        obj = {}
        obj['id'] = self.id
        obj['x'] = self.x
        obj['size'] = self.width
        obj['y'] = self.y
        return obj
