#!/usr/bin/python3
"""this module representes load_from_json_file() function"""

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    str = load_from_json_file("add_item.json")

    print(str)
    str += argv[1:]
    save_to_json_file(str, "add_item.json")

except FileNotFoundError:
    save_to_json_file(argv[1:], "add_item.json")
