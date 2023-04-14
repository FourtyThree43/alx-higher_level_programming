#!/usr/bin/python3
"""Module Pascal's Triangle function."""


def pascal_triangle_1(n):
    """
    Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        prev_row = triangle[-1]
        curr_row = [1]
        for i in range(len(prev_row)-1):
            curr_row += [prev_row[i] + prev_row[i + 1]]
        curr_row += [1]
        triangle.append(curr_row)
    return triangle


def factorial(n):
    """function to calculate factorial of a number"""
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def pascal_triangle_2(n):
    """
    Calculating Pascal's triangle using the binomial theorem:
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            value = factorial(i) // (factorial(j) * factorial(i - j))
            row.append(value)
        triangle.append(row)

    return triangle


def pascal_triangle(n):
    """
    Generates Pascal's triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(n - 1):
        prev_row = triangle[-1]
        curr_row = [sum(pair) for pair in zip([0] + prev_row, prev_row + [0])]
        triangle.append(curr_row)

    return triangle
