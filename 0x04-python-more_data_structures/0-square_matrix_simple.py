#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[elems**2 for elems in rows] for rows in matrix]
    return new
