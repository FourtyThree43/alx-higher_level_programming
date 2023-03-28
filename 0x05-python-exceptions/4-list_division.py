#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for element in range(list_length):
        try:
            result = my_list_1[element] / my_list_2[element]
        except TypeError:
            print("Wrong Type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    return result_list
