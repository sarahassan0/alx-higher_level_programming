#!/usr/bin/python3
"""this module representes save_to_json_file() function"""

import json


def save_to_json_file(my_obj, filename):
    """
    translate Python data structure into JSON string
    and write this string to a text file
    """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
