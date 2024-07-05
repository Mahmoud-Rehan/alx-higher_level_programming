#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ find_peak Function """
    if not list_of_integers:
        return (None)

    low = 0
    high = len(list_of_integers) - 1

    while low <= high:
        middle = (low + high) // 2
        peak = list_of_integers[middle]

        if (middle == 0 or peak >= list_of_integers[middle - 1]) and \
           (middle == len(list_of_integers) - 1 or
           peak >= list_of_integers[middle + 1]):
            return (peak)
        elif middle > 0 and list_of_integers[middle - 1] > peak:
            high = middle - 1
        else:
            low = middle + 1

    return (None)
