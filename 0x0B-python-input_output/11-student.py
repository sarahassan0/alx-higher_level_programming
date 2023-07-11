#!/usr/bin/python3
"""this module representes Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of instance"""

        json_dict = self.__dict__
        if attrs is None:
            return json_dict

        new_dict = {}
        for key in attrs:
            if key in json_dict:
                new_dict[key] = json_dict.get(key)
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, val in json.items():
            if hasattr(self, key):
                setattr(self, key, val)
