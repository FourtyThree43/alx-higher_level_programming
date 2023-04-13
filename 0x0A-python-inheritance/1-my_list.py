#!/usr/bin/python3
'''Module class MyList that inherits from list'''


class MyList(list):
    """
    A class that inherits from the built-in list class and adds a
    method to print the list in ascending order.
    """

    def print_sorted(self):
        '''Prints the list, but sorted (ascending sort)'''
        print(sorted(self))
