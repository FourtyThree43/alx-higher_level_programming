#!/usr/bin/env python3
if __name__ == "__main__":
    # import the functions from calculator_1 .py
    from calculator_1 import add, sub, mul, div

# define the variables a and b
a = 10
b = 5

result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

print("{:d} + {:d} = {:d}".format(a, b, result_add))
print("{:d} - {:d} = {:d}".format(a, b, result_sub))
print("{:d} * {:d} = {:d}".format(a, b, result_mul))
print("{:d} / {:d} = {:d}".format(a, b, result_div))
