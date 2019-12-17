#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in range(0, len(matrix)):
        for elems in range(0, len(matrix[rows])):
            if elems < len(matrix[rows]) - 1:
                print('{:d}'.format(matrix[rows][elems]), end=' ')
            else:
                print('{:d}'.format(matrix[rows][elems]))
        if not matrix[rows]:
            print('')
