#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a += (0, 0)
    elif len(tuple_a) == 1:
        tuple_a += (0, )
    if len(tuple_b) == 0:
        tuple_b += (0, 0)
    elif len(tuple_b) == 1:
        tuple_b += (0, )
    return tuple(x + y for x, y in zip(tuple_a[:2], tuple_b[:2]))
