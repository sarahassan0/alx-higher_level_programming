#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list is not None:
        list = []
        for i in my_list:
            list[i] = True if (i % 2 == 0) else False
            return list
