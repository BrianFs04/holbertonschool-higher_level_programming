#!/usr/bin/python3
'''
This is the 'lazy_matrix_mul' module
'''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''
    Returns the multiplication of 2 matrices
    '''
    return (np.matmul(m_a, m_b))
