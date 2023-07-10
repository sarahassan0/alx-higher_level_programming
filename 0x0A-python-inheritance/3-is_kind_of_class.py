#!/usr/bin/python3
"""is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance of 
        a class that inherited from, the specified class ; otherwise False.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    """
    return isinstance(obj, a_class)
