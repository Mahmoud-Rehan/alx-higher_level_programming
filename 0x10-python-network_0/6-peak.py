#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ find_peak Function """
    if list_of_integers == []:
        return (None)

    length = len(list_of_integers)

    if length == 0:
        return (None)
    elif length == 1:
        return (list_of_integers[0])
    elif length == 2:
        return (max(list_of_integers))

    middle = int(length / 2)
    peak = list_of_integers[middle]
    my_list = list_of_integers


    if peak > my_list[middle - 1] and peak > my_list[middle + 1]:
        return (peak)
    elif peak < my_list[middle - 1]:
        return (find_peak(my_list[:middle]))
    else:
        return (find_peak(my_list[middle + 1:]))
