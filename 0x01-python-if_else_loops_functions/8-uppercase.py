#!/usr/bin/python3
def islower(c):
    if (ord(c) >= 97 and ord(c) <= 123):
        return True
    else:
        return False


def uppercase(str):
    for i in str:
        if (islower(i)):
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print("")
