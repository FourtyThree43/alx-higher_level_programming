#!/usr/bin/python3
# prints the ASCII alphabet, in lowercase
# ASCII code of the character codes for 'a' and 'z' is between 97 and 122
for alpha_letters in range(97, 123):
    print("{}".format(chr(alpha_letters)), end="")
