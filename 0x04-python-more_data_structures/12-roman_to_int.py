#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    dictionary = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    n = 0
    for i in reversed(roman_string):
        n = dictionary[i]
        number += n if number < n * 5 else -n
    return number
