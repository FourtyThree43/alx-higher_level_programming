#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_sort = sorted(list(a_dictionary.keys()))
    for key in keys_sort:
        print("{}: {}".format(key, a_dictionary[key]))
