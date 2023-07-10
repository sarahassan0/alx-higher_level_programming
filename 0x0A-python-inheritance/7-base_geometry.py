#!/usr/bin/python3
"""base_geometry module"""


class BaseGeometry(object):
    """BaseGeometry class"""

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate the value
        Args:
            name: name
            value: value
        Raise:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
