#!/usr/bin/python3
class Square:
    '''Class
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''Constructor
        '''
        self.size = size
        self.position = position

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
        else:
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
        if not isinstance(value, tuple) or len(value) != 2\
           or type(value[0]) != int or type(value[1]) != int\
                or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        '''Returns the current square area
        '''
        return(self.size**2)

    def my_print(self):
        '''Prints in stdout the square with the character '#'
        '''
        if self.__size == 0:
            print('')
        else:
            print('\n'*self.__position[1], end='')
            for i in range(self.size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)
