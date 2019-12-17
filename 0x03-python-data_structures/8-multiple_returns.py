#!/usr/bin/python3
def multiple_returns(sentence):
    char = ''
    leng = 0
    if not sentence:
        char = None
    else:
        char = sentence[0]
        leng = len(sentence)
    return leng, char
