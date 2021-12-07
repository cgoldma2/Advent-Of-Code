#!/usr/bin/env python3

import sys


def main():
    # Set initial previous value to infinity
    prev = float("inf")
    increase_count = 0
    for num in sys.stdin:
        curr = int(num)
        if curr > prev:
            increase_count += 1
        prev = curr
    print(increase_count)


if __name__ == "__main__":
    main()

