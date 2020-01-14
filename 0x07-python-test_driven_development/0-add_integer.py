#!/usr/bin/python3
'''
This is the "add_integer" module
>>> add_integer(1, 2)
3
'''


def add_integer(a, b=98):
    '''
    Returns the addition of a and b, an integer
    '''
    if not type(a) in (int, float):
        raise TypeError('a must be an integer')
    if not type(b) in (int, float):
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is int:
        b = int(b)
    return a + b
