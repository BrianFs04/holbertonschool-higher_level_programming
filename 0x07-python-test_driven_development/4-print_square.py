#!/usr/bin/python3
'''
This is the 'print_square' module
>>> print_square(1)
#
'''


def print_square(size):
    '''
    Prints a square in accordance with the size with the character '#'
    '''
    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    hashy = size*'#'

    for i in range(size):
        print(hashy)
