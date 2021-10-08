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
    for l_a in m_a:
        if not isinstance(l_a, list):
            raise TypeError("m_a must be a list of lists")
        if len(l_a) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for l_b in m_b:
        if not isinstance(l_b, list):
            raise TypeError("m_b must be a list of lists")
        if len(l_b) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    for m in m_a:
        for x in m:
            if type(x) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for n in m_b:
        for y in n:
            if type(y) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

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
