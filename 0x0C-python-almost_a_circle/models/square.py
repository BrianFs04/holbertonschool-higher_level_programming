#!/usr/bin/python3
'''
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square class
    '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Constructor
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' Str method
        '''
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        ''' Getter size
        '''
        return self.width

    @size.setter
    def size(self, value):
        ''' Setter size
        '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' Assigns an argument to each attribute
        '''
        listy = ['id', 'size', 'x', 'y']
        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                setattr(self, listy[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        ''' Returns the dictionary representation of Rectangle class
        '''
        dicty = {'id': self.id, 'size': self.size, 'x': self.x,
                 'y': self.y}
        return dicty
