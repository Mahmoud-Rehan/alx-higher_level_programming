#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return (0)
    else:
        n = sum(x * y for x, y in my_list)
        weight = sum(y for x, y in my_list)
        return (n / weight)
