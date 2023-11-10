#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_num = 0
    key = None
    for k, v in a_dictionary.item():
        if v > max_num:
            max_num = v
            key = k
    return key
