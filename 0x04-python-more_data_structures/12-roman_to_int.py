#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    for n in reversed(roman_string):
        v = roman_nums[n]
        if v < prev:
            result -= v
        else:
            result += v
        prev = v
    return (result)
