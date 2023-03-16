#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    Computes the square value of all integers in a matrix.

    Args:
        matrix: A 2D array of integers.

    Returns:
        A new matrix with the same size as the input matrix, where each
        value is the square of the corresponding value in the input matrix.
        The input matrix is not modified.
    '''
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return (new_matrix)
