#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for i, n in enumerate(new_list):
        if n == search:
            new_list[i] = replace
    return (new_list)
