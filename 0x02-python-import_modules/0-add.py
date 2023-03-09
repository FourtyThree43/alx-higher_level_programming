#!/usr/bin/env python3
if __name__ == "__main__":
    # import the function add from add_0.py
    from add_0 import add

# define the variables a and b
a = 1
b = 2

result_add = add(a, b)
print("{:d} + {:d} = {:d}".format(a, b, result_add))
