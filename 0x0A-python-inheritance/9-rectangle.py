#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class Rectangle with inheritance
    '''
    def __init__(self, width, height):
        '''Constructor
        '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        '''Prints a description
        '''
        msg = '[Rectangle] {}/{}'.format(self.__width, self.__height)
        return msg

    def area(self):
        '''Area method
        '''
        rec_area = self.__width * self.__height
        return rec_area
