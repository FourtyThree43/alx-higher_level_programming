#!/usr/bin/python3
'''Module lookup the list of available attributes and methods of an object:'''


def lookup(obj):
    '''Returns the list of available attributes and methods of an object'''
    return sorted(dir(obj))
