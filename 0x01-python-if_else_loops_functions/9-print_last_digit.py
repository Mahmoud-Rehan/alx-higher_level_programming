#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        n = (number % -10) * -1
        print("{}".format(n), end="")
        return (n)
    else:
        print("{}".format(number % 10), end="")
        return (number % 10)
