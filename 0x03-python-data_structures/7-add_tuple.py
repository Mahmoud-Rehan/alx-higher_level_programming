#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new1 = tuple_a[0] if len(tuple_a) > 0 else 0
    new2 = tuple_a[1] if len(tuple_b) > 1 else 0
    new3 = tuple_b[0] if len(tuple_b) > 0 else 0
    new4 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (new1 + new3, new2 + new4)
