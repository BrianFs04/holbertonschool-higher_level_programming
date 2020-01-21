#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    '''Reads n lines of a text file
    '''
    i = 0
    with open(filename) as f:
        if nb_lines <= 0:
            lines = f.read()
            print(lines, end='')
        else:
            for lines in f:
                i += 1
                print(lines, end='')
                if i == nb_lines:
                    break
