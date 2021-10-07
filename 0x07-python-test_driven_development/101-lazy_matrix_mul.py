#!/usr/bin/python3
'''
    multiplies two matrices with numpy
'''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''
        multiplies m_a with m_b
    '''
    return np.matmul(m_a, m_b)
