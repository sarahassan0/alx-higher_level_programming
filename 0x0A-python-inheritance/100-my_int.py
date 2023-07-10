#!/usr/bin/python3
"""my_int module defines a class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Override == opeartor with != behavior"""
        """
        self.real: is the real part of the MyInt object compares with the value
            passed to the method
        """
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return not super().__ne__(value)
