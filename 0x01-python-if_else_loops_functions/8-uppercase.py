#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        c = ord(str[i])
        if c >= 97 and c <= 122:
            a = chr(c - 32)
        elif c >= 65 and c <= 90:
            a = chr(c)
        elif c >= 48 and c <= 57:
            a = chr(c)
        elif c == 32:
            a = ' '
        print('{}'.format(a), end='')
    print('')
