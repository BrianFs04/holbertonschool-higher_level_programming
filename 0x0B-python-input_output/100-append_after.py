#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    '''Inserts a line of text to a file, after
    each line containing a specific string
    '''
    sentence = ''
    with open(filename, 'r+') as f:
        for word in f:
            sentence += word
            if search_string in word:
                sentence += new_string
        f.seek(0)
        f.write(sentence)
