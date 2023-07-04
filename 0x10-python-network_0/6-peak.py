#!/usr/bin/python3
"""Defines function find_peak."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers with Binary search algorithm
    """
    n = len(list_of_integers)

    if n == 0:
        return None

    start_index = 0
    end_index = n - 1

    while start_index < end_index:
        mid_index = (start_index + end_index) // 2

        if list_of_integers[mid_index] < list_of_integers[mid_index + 1]:
            start_index = mid_index + 1
        else:
            end_index = mid_index

    return list_of_integers[start_index]
