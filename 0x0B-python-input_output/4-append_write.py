#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, 'a+') as f:
        appe_s = f.write('Holberton School is so cool!\n')
    return appe_s
