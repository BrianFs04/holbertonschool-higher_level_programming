#!/usr/bin/python3
class Square:
    '''Class
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''Constructor
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        if isinstance(position, tuple):
            for i in position:
                if not isinstance(i, int) or i < 0:
                    raise TypeError('position must be a tuple of 2'
                                    ' positive integers')
        self.__position = position

    @property
    def size(self):
        '''Getter
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        '''Getter
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''Setter
        '''
        if isinstance(value, tuple):
            for i in value:
                if not isinstance(i, int) or i < 0:
                    raise TypeError('position must be a tuple of 2'
                                    ' positive integers')
        self.__position = value

    def area(self):
        '''Returns the current square area
        '''
        return(self.size**2)

    def my_print(self):
        '''Prints in stdout the square with the character '#'
        '''
        if self.size == 0:
            print()
        for i in range(self.size):
            print(' '*self.position[0], end='')
            print('#'*self.size)
