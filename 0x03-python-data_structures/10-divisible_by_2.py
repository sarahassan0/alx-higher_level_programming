#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list = my_list[:]
    for i in my_list:
        list[i] == True if (i % 2 == 0) else False
        return list
