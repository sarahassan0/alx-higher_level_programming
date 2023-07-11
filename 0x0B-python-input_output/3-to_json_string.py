#!/usr/bin/python3
"""this module representes to_json_string() function"""

import json


def to_json_string(my_obj):
    """translate Python data structure into JSON string"""
    return json.dumps(my_obj)
