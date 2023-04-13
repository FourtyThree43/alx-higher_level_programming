#!/usr/bin/python3
'''
script that adds all arguments to a Python list,
and then save them to a file
'''
import sys


if __name__ == "__main__":
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        item = load_from_json_file("add_item.json")
    except FileNotFoundError:
        item = []
    item.extend(sys.argv[1:])
    save_to_json_file(item, "add_item.json")
