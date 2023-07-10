#!/usr/bin/python3
"""add_attribute module"""


def add_attribute(obj, att, value):
    """
    Add a new attribute to an object if possible
    this also can be done by checking if the oblect has __dict__ atrribute
    using dir() function
    __dict__ it typically means that it is an instance of a custom class
    that allows dynamically adding new attributes

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
