#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if ((j != 0 or i != 1) and (j != i)):
            print("{:d}{:d}".format(i, j), end="")
            if (i != 9 or j != 8):
                print(", ", end="")
print()
