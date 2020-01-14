#!/usr/bin/python3
'''
This is 'say_my_name' module
>>> say_my_name('Betty', 'Holberton')
My name is Betty Holberton
'''


def say_my_name(first_name, last_name=""):
    '''
    Returns 'My name is ' plus the concatenation
    between first_name and last_name
    '''

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print('My name is {:s} {:s}'.format(first_name, last_name))
