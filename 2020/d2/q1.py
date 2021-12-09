#!/usr/bin/env python3

import sys


def main():
    valid = 0
    for line in sys.stdin:
        line = line.split()
        low, high = map(int, line[0].split('-'))
        char = line[1][0]
        password = line[2]

        count = sum(c == char for c in password)
        valid += count >= low and count <= high

    print(valid)

if __name__ == "__main__":
    main()

