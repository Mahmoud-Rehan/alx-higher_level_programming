#!/usr/bin/python3
for n in range(122, 96, -1):
    if n % 2 == 1:
        n = n - 32
    print("{:c}".format(n), end="")
