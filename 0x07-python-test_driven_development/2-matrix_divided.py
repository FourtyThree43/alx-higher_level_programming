#!/usr/bin/python3
''' Module to divide a matrix'''


def matrix_divided(matrix, div) -> list | int | float:
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): a list of lists of integers or floats.
        div (int or float): the number to divide all elements of the matrix by.

    Returns:
        list: a new matrix with all elements divided by div
        and rounded to 2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of integers or floats,
                   or if div is not a number.
        ZeroDivisionError: if div is equal to 0.
        TypeError: if each row of matrix is not of the same size.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists of integers/floats")
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError("matrix must be a list of lists of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
