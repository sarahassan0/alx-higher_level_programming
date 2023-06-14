#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for num in my_list:
        new_list.append(num if num != search else replace)
    return (new_list)
