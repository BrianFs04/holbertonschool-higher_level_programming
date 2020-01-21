#!/usr/bin/python3
def number_of_lines(filename=""):
    '''Returns: # of lines of a text file
    '''
    with open(filename) as f:
        return sum(1 for lines in f)
