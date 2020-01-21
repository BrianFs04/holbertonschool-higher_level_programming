#!/usr/bin/python3
def write_file(filename="", text=""):
    '''Writes a string to a text file
    '''
    with open(filename, 'w') as f:
        add_s = f.write(text)
    return add_s
