#!/usr/bin/python3
def islower(c):
    if (ord(c) >= 97 and ord(c) <= 123):
        return True
    else:
        return False


def uppercase(str):
    for i in str:
            print("{:c}"
                .format(ord(i) if not islowe(i) else ord(i) - 32,
                end="")
    print()
