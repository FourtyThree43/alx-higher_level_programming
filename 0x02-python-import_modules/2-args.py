#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

if len(argv) == 1:
    print("{:d} arguments.".format(len(argv) - 1))
else:
    if len(argv) == 2:
        print("{:d} argument:".format(len(argv) - 1))
    else:
        print("{:d} arguments:".format(len(argv) - 1))

    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))
