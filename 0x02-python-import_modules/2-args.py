#!/usr/bin/pytho3

from sys import argv

if len(argv) == 1:
    print("0 argumets.")
elif len(argv) == 2:
    print("1 argument:")
    print("1: {}".format(argv[1]))
else:
    print("{} arguments:".format(len(argv)))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
