#!/usr/bin/python3
class Square:
    '''Class
    '''
    def __init__(self, size=0):
        '''Constructor
        '''
        self.__size = size

    @property
    def size(self):
        '''Getter
        '''
        return(self.__size)

    @size.setter
    def size(self, value):
        '''Setter
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        '''Returns the current square data
        '''
        return(self.size**2)
