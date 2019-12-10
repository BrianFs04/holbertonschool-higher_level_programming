#!/usr/bin/python3
def uppercase(str):
    a = ''
    for i in range(len(str)):
        c = ord(str[i])
        if c >= 97 and c <= 122:
            a = chr(c - 32)
        elif c >= 65 and c <= 90:
            a = chr(c)
        else:
            a = chr(c)
        print('{}'.format(a), end='')
    print('')
