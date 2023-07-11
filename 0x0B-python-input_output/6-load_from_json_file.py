#!/usr/bin/python3
"""this module representes load_from_json_file() function"""

import json


def load_from_json_file(filename):
    """ creates a pthion object from a JSON file"""

    with open(filename, "r", encoding="utf-8") as file:
        obj = json.loads(file)
