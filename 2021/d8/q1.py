#!/usr/bin/env python3

import sys


def main():
    instances = 0
    while line := sys.stdin.readline():
        pattern, output = line.split('|')
        pattern = pattern.split()
        output = output.split()
        for out in output:
            l = len(out)
            if l <= 4 or l == 7:
                instances += 1
    print(instances)


if __name__ == "__main__":
    main()

