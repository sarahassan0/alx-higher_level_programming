#!/usr/bin/python3
""" This module represents A Square class """


class Square:
    """ A square class"""

    def __init__(self, size):
        """
        init function initalizes the square.

        Args:
            size (int): The size of a square.
        """
        if (type(size)) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
