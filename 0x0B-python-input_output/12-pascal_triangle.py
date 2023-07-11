#!/usr/bin/python3
"""this module representes append_after dunction"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s
        triangle of n:
    """
    if n <= 0:
        return []

    trg = [[1]]
    while len(trg) != n:
        t = trg[-1]
        tp = [1]
        for i in range(len(t) - 1):
            tp.append(t[i] + t[i + 1])
        tp.append(1)
        trg.append(tp)
    return trg
