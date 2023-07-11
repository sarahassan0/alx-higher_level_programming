#!/usr/bin/python3
"""this module representes to_json_string() function"""

import json


def from_json_string(my_str):
    """translate a string containing JSON data into a Python value"""
    return json.loads(my_str)
