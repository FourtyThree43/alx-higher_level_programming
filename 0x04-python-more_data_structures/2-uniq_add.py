#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)

    Args:
        my_list (list): The list of integers to add.

    Returns:
        int: The sum of all unique integers in the list.

    """
    uniq_integers = set(my_list)
    return sum(uniq_integers)
