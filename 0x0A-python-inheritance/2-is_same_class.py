#!/usr/bin/python3
"""is_the_same_class module"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specific class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified class,
        otherwise False.
    """
    return type(obj) == a_class
