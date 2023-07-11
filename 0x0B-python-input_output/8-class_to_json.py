#!/usr/bin/python3
"""this module representes class_to_json() function"""


def class_to_json(obj):
    """
    class_to_json
    Returns a dictionary representation of an object's attributes
        for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representing the attributes of the object.
    """
    return obj.__dict__
