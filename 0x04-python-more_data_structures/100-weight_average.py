#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        score, weight = 0, 0
        for i in my_list:
            score += i[0] * i[1]
            weight += i[1]
        return score/weight
