#!/usr/bin/python3

def print_square(size):
    '''Prints a sized square of '#',
    size must be an integer and >= 0
    '''
    if (not isinstance(size, int)) or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print('#', end="")
        print()
