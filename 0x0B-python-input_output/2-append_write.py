#!/usr/bin/python3
'''Module that appends a string at the end of a text file (UTF8)'''


def append_write(filename="", text=""):
    '''
    A function that appends a string at the end of a text file (UTF8)

    Args:
        filename - name of the file to write to.
        text(str) - the string to write
    Returns:
        the number of characters added:
    '''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
