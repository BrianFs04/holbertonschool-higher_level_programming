#!/usr/bin/python3
for numbers in range(0, 10):
    for repeated_numbers in range(0, 10):
        if numbers < repeated_numbers:
            if numbers == 8 and repeated_numbers == 9:
                print('{}{}'.format(numbers, repeated_numbers), end='')
            else:
                print('{}{}, '.format(numbers, repeated_numbers), end='')
print('')
