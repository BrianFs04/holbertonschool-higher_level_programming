#!/usr/bin/python3
class BaseGeometry:
    '''Class BaseGeometry
    '''
    def area(self):
        '''Public instance method that raises an
        exception
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Public instance method that validate value
        '''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
