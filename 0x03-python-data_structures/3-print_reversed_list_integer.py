#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list)
    while i > 0:
        print('{:d}'.format(i), end='\n')
        i -= 1
