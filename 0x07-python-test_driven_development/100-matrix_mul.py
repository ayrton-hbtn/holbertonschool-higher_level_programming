#!/usr/bin/python3
'''
    Matrix multiplication
'''


def matrix_mul(m_a, m_b):
    '''
        Multiplies m_a with m_b, matrices
        can't be empty and elements
        must be int or float
    '''
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty") 
    for l in m_a:
        if not isinstance(l, list):
            raise TypeError("m_a must be a list of lists")
        if len(l) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        if len(l) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")
    for l in m_b:
        if not isinstance(l, list):
            raise TypeError("m_b must be a list of lists")
        if len(l) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    for l in m_a:
        for x in l:
            if type(x) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for l in m_b:
        for x in l:
            if type(x) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    matrix = []
    for i in range(len(m_a)):
        result = []
        for j in range(len(m_b[0])):
            res = 0
            for k in range(len(m_b)):
                res += m_a[i][k] * m_b[k][j]
            result.append(res)
        matrix.append(result)

    return matrix
