#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """Retrieve a list of attributes and methods of an object"""
    return list(dir(obj))
