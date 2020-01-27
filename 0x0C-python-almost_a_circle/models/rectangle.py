#!/usr/bin/python3
from models.base import Base
'''
'''


class Rectangle(Base):
    ''' Rectangle class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.__x, self.__y, self.__width, self.__height)


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be > 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be > 0')
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        if self.__y is not 0:
            print('\n'*self.__y, end='')
        for i in range(self.__height):
            print('{}{}'.format(' '*self.__x, '#'*self.__width))

    def update(self, *args, **kwargs):
        listy = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                setattr(self, listy[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        dicty = {'id': self.id, 'width': self.__width, 'height': self.__height,
                 'x': self.__x, 'y': self.__y}
        return dicty
