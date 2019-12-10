#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)
if int(last[-1:]) > 5:
    print('Last digit of {:d} is {:s} and is greater than 5'.format(number, last[-1:]))
elif int(last[-1:]) == 0:
    print('Last digit of {:d} is {:s} and is 0'.format(number, last[-1:]))
else:
    print('Last digit of {:d} is {:s} and is less than 6 and not 0'.format(number, last[-1:]))
