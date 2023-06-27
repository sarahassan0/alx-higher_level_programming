#!/usr/bin/python3
""" This module represents A Square class """


class Square:
    """ A square class"""

    def __init__(self, size=0):
        """
        init function initalizes the square.
        Args:
            size (int): The size of a square.
        """
        self.__size = size

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """ prints the square """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)

    def area(self):
        return self.__size * self.__size
