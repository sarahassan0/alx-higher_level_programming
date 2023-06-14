#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        max = sorted(a_dictionary.values())[-1]
        for key in a_dictionary:
            if a_dictionary[key] is not None and a_dictionary[key] == max:
                return (key)
    return None
