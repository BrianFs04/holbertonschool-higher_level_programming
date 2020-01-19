#!/usr/bin/python3
'''
This is the 'matrix_mul' module
>>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
[[7, 10], [15, 22]]
'''


def matrix_mul(m_a, m_b):
    '''
    Returns the multiplication of 2 matrices
    '''
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    for rows_a in m_a:
        if type(rows_a) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(rows_a) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
        for colums_a in rows_a:
            if not type(colums_a) in (int, float):
                raise TypeError('m_a should contain only integers or floats')

    for rows_b in m_b:
        if type(rows_b) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(rows_b) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')
        for colums_b in rows_b:
            if not type(colums_b) in (int, float):
                raise TypeError('m_b should contain only integers or floats')

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(rows_a, col_b))
               for col_b in zip(*m_b)] for rows_a in m_a]

    return result
