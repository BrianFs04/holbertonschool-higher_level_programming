#!/usr/bin/python3


class MyInt(int):
    '''Class MyInt
    '''
    def __ne__(int, other):
        '''Rich comparison for !=
        '''
        return True

    def __eq__(int, other):
        '''Rich comparison for ==
        '''
        return False
