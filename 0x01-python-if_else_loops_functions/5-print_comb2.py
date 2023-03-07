#!/usr/bin/python3
# prints numbers from 0 to 98 separated by , .
for i in range(100):
    print('{:02d}'.format(i), end=", " if i < 99 else '\n')
