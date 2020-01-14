#!/usr/bin/python3
class Rectangle:
    '''Class Rectangle
    '''
    def __init__(self, width=0, height=0):
        '''Constructor
        '''
        self.__width = width
        self.__height = height

    def __str__(self):
        '''Str method
        '''
        empty = ''

        if self.width is 0 or self.height is 0:
            return empty

        for i in range(self.height):
            empty += '#'*self.width
            empty += '\n'

        return(empty[:-1])

    @property
    def width(self):
        '''Width getter
        '''
        return(self.__width)

    @width.setter
    def width(self, value):
        '''Width setter
        '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''Height getter
        '''
        return(self.__height)

    @height.setter
    def height(self, value):
        '''Height setter
        '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        ''' Public instance method that
        returns the rectangle area
        '''
        return(self.width * self.height)

    def perimeter(self):
        ''' Public instance method that
        returns the rectangle perimeter
        '''
        if self.width is 0 and self.height is 0:
            return(0)
        else:
            return(self.width*2 + self.height*2)
