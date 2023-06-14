#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        max = sorted(a_dictionary.values())[-1]
        for key in a_dictionary:
            if a_dictionary[key] == max:
                return key
