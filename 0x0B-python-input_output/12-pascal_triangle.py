#!/usr/bin/python3
'''
Pascal triangle
'''


def pascal_triangle(n):
    '''
    Pascal triangle
    '''
    triangle = [[1]]
    prev = []
    current = 0
    if n <= 0:
        return prev
    while n >= 2:
        prev = triangle[current]
        row = [1]
        for i in range(len(prev)):
            try:
                row.append(prev[i] + prev[i + 1])
            except Exception:
                row.append(1)
        triangle.append(row)
        current += 1
        n -= 1
    return triangle
