#!/usr/bin/python3
"""this module representes write_file() function"""


def write_file(filename="", text=""):
    """write to text file"""

    with open(filename, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
    return num_chars_written
