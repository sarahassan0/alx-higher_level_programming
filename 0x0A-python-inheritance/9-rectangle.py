#!/usr/bin/python3
"""rectangle module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """initializes a Rectangle with it's dimensions and validate them"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculates area"""
        return self.__width * self.__height

    def __str__(self):
        "returns a formatted representation of the Rectangle"
        s = f"[{str(self.__class__.__name__)}] {self.__width}/{self.__height}"
        return s
