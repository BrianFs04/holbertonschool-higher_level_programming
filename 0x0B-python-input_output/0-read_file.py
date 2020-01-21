#!/usr/bin/python3
def read_file(filename=""):
    '''Reads a text file
    '''
    with open(filename) as f:
        lines = f.read()
    print(lines, end='')
