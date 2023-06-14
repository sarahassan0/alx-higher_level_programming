#!/usr/bin/pythin3

def square_matrix_simple(matrix=[]):
    # [[num**2 for num in x] for x in matrix]
    return [list(map(lambda num: num * num, x)) for x in matrix]
