#!/usr/bin/bash
def safe_print_list_integers(my_list=[], x=0):
    element_count = 0
    for element in my_list:
        try:
            if type(element) == int:
                print("{:d}".format(element), end=" ")
                element_count += 1
        except (IndexError, ValueError):
            pass
        if element_count >= x:
            break
    print()
    return element_count
