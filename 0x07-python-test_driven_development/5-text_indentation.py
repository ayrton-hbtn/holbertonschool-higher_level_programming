#!/usr/bin/python3

def text_indentation(text):
    ''' Prints text with 2 new lines after each
    of the following characters: . , ? :
    no spaces at beginning or end of each line
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    a = ""
    chars = ['.', '?', ':']
    for c in text:
        a += c
        if c in chars:
            print(a.lstrip())
            print()
            a = ""
    if not any(c in a for c in chars):
        print(a.lstrip(), end="")
