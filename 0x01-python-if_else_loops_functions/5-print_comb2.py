#!/usr/bin/python3
for numbers in range(00, 100):
    if numbers >= 0 and numbers <= 98:
        print('{:02d}, '.format(numbers), end = '')
    else:
        print('{}'.format(numbers), end = '')
