#!/usr/bin/python3
"""this module representes append_write() function"""


def append_write(filename="", text=""):
    """append to text file"""

    with open(filename, "a", encoding="utf-8") as file:
        num_chars_written = file.write(text)
    return num_chars_written
