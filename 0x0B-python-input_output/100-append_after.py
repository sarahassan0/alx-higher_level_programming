#!/usr/bin/python3
"""this module representes append_after dunction"""


def append_after(filename="", search_string="", new_string=""):
    """appends new_string after a line containing
        search_string in file """

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        i = 0

        for line in lines:
            i += 1
            if search_string in line:
                lines.insert(i + 1, new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
