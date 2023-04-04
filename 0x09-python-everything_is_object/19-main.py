#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list
print("--------------------")

my_list = [1, 2, 3]
print("my_list")
print(my_list)

print("--------------------")

new_list = copy_list(my_list)
print("my_list ==> ", end='')
print(my_list)
print("new_list => ", end='')
print(new_list)

print("--------------------")

print('new_list == my_list')
print(new_list == my_list)
print('new_list is my_list')
print(new_list is my_list)

print("--------------------")