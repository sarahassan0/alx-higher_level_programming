#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ represent a rectangle class """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ initialize a new Rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return the Rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """return the Rectangle perimeter """
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.height + self.width) * 2)

    def __str__(self):
        """ return the string representation of the Rectangle with # char """
        str = ""
        if self.width == 0 or self.height == 0:
            return str

        for i in range(self.height):
            for j in range(self.width):
                str += "#"
            if i != self.height - 1:
                str += "\n"
        return str

    def __repr__(self):
        """ return the official string representation of the Rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ print 'Bye rectangle...' for every deletion of a Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
