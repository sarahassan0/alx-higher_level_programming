#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # {key : value * 2 for key, value in a_dictionary.items()}
    return {key: a_dictionary[key] * 2 for key in a_dictionary}
