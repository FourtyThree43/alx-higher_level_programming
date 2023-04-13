#!/usr/bin/python3
"""Module load form json file"""
import json


def load_from_json_file(filename):
    '''
    function that creates an Object from a “JSON file”
    '''
    with open(filename) as f:
        json_str = f.read()
        obj = json.loads(json_str)
        return obj
