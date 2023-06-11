#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a_num1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a_num2 = tuple_a[1] if len(tuple_a) > 1 else 0

    b_num1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b_num2 = tuple_b[1] if len(tuple_b) > 1 else 0

    return ((a_num1+b_num1, a_num2+b_num2))
