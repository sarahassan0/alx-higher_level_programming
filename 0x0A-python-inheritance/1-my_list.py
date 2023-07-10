#!/usr/bin/python3
"""my_list module"""


class MyList(list):
    """MyList class inherits from list class"""

    def print_sorted(self):
        """print the list in ascending order"""
        print(sorted(self))
