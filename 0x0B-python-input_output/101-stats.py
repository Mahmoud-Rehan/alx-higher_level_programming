#!/usr/bin/python3
""" MODULE FOR READING stdin """
from sys import stdin

status = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }

size = n = 0


def print_size():
    """ printer function """
    print("File size: {}".format(size))
    for k, v in sorted(status.items()):
        if v > 0:
            print("{:s}: {:d}".format(k, v))


try:
    for line in stdin:
        split = line.split()
        if len(split) >= 2:
            s = split[-2]
            size += int(split[-1])
            if s in status:
                status[s] += 1
        n += 1

        if n % 10 == 0:
            print_size()
        print_size()
except KeyboardInterrupt as r:
    print_size()
