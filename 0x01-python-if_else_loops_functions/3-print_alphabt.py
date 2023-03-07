#!/usr/bin/python3
for alpha_letters in range(97, 123):
    if alpha_letters == 101 or alpha_letters == 113:
        continue
    print("{}".format(chr(alpha_letters)), end="")
