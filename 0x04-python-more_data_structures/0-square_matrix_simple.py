#!/usr/bin/pythin3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda num: num * num, x)) for x in matrix]
