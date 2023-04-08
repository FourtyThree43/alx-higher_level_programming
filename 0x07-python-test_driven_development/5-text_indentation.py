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

    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[i])
            if i < len(text) - 1 and text[i+1] == " ":
                i += 1
            print("\n")
        else:
            print(text[i], end="")
