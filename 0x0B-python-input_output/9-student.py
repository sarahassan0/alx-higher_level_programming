#!/usr/bin/python3
"""this module representes Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary representation of instance"""
        return self.__dict__
