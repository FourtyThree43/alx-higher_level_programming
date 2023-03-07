#!/usr/bin/python3
def uppercase(str):
    # To Convert ASCII to uppercase: (ord(c) - 32) i.e for a is (97-32) 65 = A.
    for c in str:
        uppercase_c = chr(ord(c) - 32) if ord(c) >= 97 and ord(c) <= 122 else c
        print('{}'.format(uppercase_c), end='')
    print()
