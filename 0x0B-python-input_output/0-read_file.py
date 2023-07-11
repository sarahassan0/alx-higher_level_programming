#!/usr/bin/python3
"""this representes read_file() function"""


def read_file(filename=""):
    """read from text file"""

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
