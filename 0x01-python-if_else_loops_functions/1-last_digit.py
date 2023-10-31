#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is ".format(number), end="")
if number >= 0:
    last_digit = number % 10
elif number < 0:
    last_digit = number % -10
if last_digit < 6 and last_digit != 0:
    print(f"{last_digit} and is less than 6 and not 0")
elif last_digit > 5:
    print(f"{last_digit} and is greater than 5")
else:
    print("{last_digit} and is 0")
