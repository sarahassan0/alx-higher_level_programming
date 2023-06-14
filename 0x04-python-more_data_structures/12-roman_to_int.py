#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    vals = [roman_dict[x] for x in roman_string]

    result = 0
    for i in range(len(vals)):
        result += vals[i]
        if vals[i] > vals[i-1] and i != 0:
            result -= (vals[i-1] * 2)
    return result
