#!/usr/bin/env python3

import sys


def main():
    valid = 0
    for line in sys.stdin:
        line = line.split()
        first, second = map(int, line[0].split('-'))
        char = line[1][0]
        password = line[2]

        present1 = password[first-1] == char
        present2 = password[second-1] == char

        valid += ((present1 or present2) and not (present1 and present2))

    print(valid)

if __name__ == "__main__":
    main()

