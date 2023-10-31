#!/usr/bin/python3
def print_last_digit(number):
    if number < 10:
        print("{:d}".format(number), end="")
        return(number)
    else:
        print("{:d}".format(number % 10), end="")
    return (number % 10)
