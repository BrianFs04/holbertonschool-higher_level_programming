#!/usr/bin/python3
def print_last_digit(number):
    if number == 0:
        print(number, end='')
        return number
    else:
        number = abs(number) % 10
        print(number, end='')
        return number
