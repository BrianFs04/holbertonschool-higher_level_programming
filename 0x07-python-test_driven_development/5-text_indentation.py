#!/usr/bin/python3
'''
This is the 'text_indentation' module
>>> text_indentation("Hi. What's your name?")
Hi.
What's your name?

'''


def text_indentation(text):
    '''
    Prints a text with 2 new lines after each of these characters: ., ? and :
    '''
    if type(text) is not str:
        raise TypeError('text must be a string')

    for letters in range(len(text)):
        if text[letters] is ' ' and text[letters - 1] in ('.', '?', ':'):
            continue

        print(text[letters], end='')

        if text[letters] in ('.', '?', ':'):
            print('\n')
