#!/usr/bin/python3


from sys import stdin


status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }

size = 0
n = 0

def print_states():
    print(f"File size: {size}")

    for k, v in sorted(status_codes.items()):
        if v > 0:
            print(f"{k}: {v}")


try:
    for line in stdin:
        split_line = line.split()

        if len(split_line) >= 2:
            status = split_line[-2]
            size = size + int(split_line[-1])
            
            if status in status_codes:
                status_codes[status] += 1

        n = n + 1

        if n % 10 == 0:
            print_states()
    print_states()

except KeyboardInterrupt as msg:
    print_states()
