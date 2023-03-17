#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", "Py" 'number': 13, 'track': "Low level", 'test': "High" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
