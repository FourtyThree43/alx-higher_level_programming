#!/usr/bin/python3
'''Module to check if object is an instance of a class that inherited from'''


def is_kind_of_class(obj, a_class):
    '''
    Returns True if obj is an instance of a_class;
    False otherwise
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
