#!/usr/bin/python3

def matrix_divided(matrix, div):
    '''Divides all elements of a matrix,
    elements must be int or float
    '''

    new_matrix = []
    new_matrix_row = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix_row.append(round(elem / div, 2))
        new_matrix.append(new_matrix_row)
        new_matrix_row = []
    return new_matrix
