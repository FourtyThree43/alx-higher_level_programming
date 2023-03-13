#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_value = my_list[0]
        for num_value in range(len(my_list)):
            if my_list[num_value] > max_value:
                max_value = my_list[num_value]
        return max_value
