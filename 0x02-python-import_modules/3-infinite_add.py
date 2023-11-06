#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{}".format(0))
    else:
        n = 0
        for i in range(1, len(argv)):
            n += int(argv[i])
        print("{}".format(n))
