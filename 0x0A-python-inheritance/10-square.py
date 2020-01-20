#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class square with inheritance
    '''
    def __init__(self, size):
        '''Constructor
        '''
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Area method
        '''
        squ_area = self.__size**2
        return squ_area
