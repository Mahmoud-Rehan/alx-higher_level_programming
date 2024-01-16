#!/usr/bin/python3
for i in range(97, 123):
    if not chr(i) == "q" and not chr(i) == "e":
        print("{}".format(chr(i)), end="")
