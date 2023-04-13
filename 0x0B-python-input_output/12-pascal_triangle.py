#!/usr/bin/python3#
"""Module Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    pas_tri = [[1]]
    while len(pas_tri) != n:
        prev_row = pas_tri[-1]
        new_row = [1]
        for i in range(len(prev_row)-1):
            new_row += [prev_row[i] + prev_row[i + 1]]
        new_row += [1]
        pas_tri.append(new_row)
    return pas_tri
