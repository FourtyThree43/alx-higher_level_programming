#!/usr/bin/python3
'''Module Text indentation'''


def text_indentation(text):
    '''
    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: input text.

    Return: print text
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = (".", "?", ":")
    last_char = ""

    for char in text:
        if char == " " and last_char in punctuation:
            continue
        print(char, end="")
        if char in punctuation:
            print("\n")
        last_char = char
