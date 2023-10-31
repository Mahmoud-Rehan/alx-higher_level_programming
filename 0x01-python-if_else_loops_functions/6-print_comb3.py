#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if ((j != 0 or i != 1) and (j != i)):
            print("{:d}{:d}".format(i, j), end="")
            if (i != 8 or j != 9):
                print(", ", end="")
print()
