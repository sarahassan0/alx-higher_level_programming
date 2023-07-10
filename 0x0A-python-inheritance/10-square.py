#!/usr/bin/python3
"""square module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class"""

    def __init__(self, size):
        """ initializes a new Square with size and validate it"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
