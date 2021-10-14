#!/usr/bin/python3
'''
Inserts a line of text to a file
after each line containing a specific string
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    If search_string is in filename, new_string is
    added in next line
    '''
    new_text = []
    with open(filename, "r") as f:
        for line in f:
            new_text.append(line)
            if search_string in line:
                new_text.append(new_string)

    with open(filename, "w") as f:
        f.writelines(new_text)
