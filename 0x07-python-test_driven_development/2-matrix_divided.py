#!/usr/bin/python3
'''
This is the 'matrix_divided' module
>>> matrix_divided([[8, 6], [4, 2]], 2)
[[4.0, 3.0], [2.0, 1.0]]
'''


def matrix_divided(matrix, div):
    '''
    Returns the division of all matrix' elements by number in div
    '''
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')

    if not type(div) in (int, float):
        raise TypeError('div must be a number')

    if div is 0:
        raise ZeroDivisionError('division by zero')

    for rows in matrix:
        if type(rows) is not list:
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
        for elems in rows:
            if not type(elems) in (int, float):
                raise TypeError('matrix must be a matrix (list of lists) '
                                'of integers/floats')

        if len(rows) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

    new_matrix = [[float("{0:.2f}".format(elem/div)) for elem in rows]
                  for rows in matrix]

    return new_matrix
