#!/usr/bin/python3
def no_c(my_string):
    repla = ''
    for i in range(0, len(my_string)):
        if my_string[i] == 'c':
            continue
        elif my_string[i] == 'C':
            continue
        else:
            repla += my_string[i]
    return repla
