#!/usr/bin/python3
"""this module representes load_from_json_file() function"""

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    list = load_from_json_file("add_item.json")

except FileNotFoundError:
    list = []

list += argv[1:]
save_to_json_file(list, "add_item.json")
