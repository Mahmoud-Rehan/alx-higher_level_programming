#!/usr/bin/python3
for n in range(97, 123):
    if n != ord('q') and n != ord('e'):
        print("{:c}".format(n), end="")
