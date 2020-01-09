#!/usr/bin/python3
class Square:
    '''Class
    '''
    def __init__(self, size=0):
        '''function that checks size as integer
        and define a private instance attribute
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''function that returns the current square
        data
        '''
        return(self.__size**2)
