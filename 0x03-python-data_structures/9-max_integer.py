#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        list = my_list[:]
        list.sort()
        return list[-1]
