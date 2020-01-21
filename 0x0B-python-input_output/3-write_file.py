#!/usr/bin/python3
def write_file(filename="", text=""):
    '''Writes a string to a text file
    '''
    with open(filename, 'w') as f:
        add_s = f.write('Holberton School is so cool!\n')
    return add_s
