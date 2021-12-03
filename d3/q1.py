#!/usr/bin/env python3

import sys


def main():
    count = 1
    l1 = sys.stdin.readline().strip()
    counts = [int(i) for i in l1]
    for line in sys.stdin:
        for i, num in enumerate(line.strip()):
            counts[i] += int(num)
        count += 1
    print(counts)
    print(count)

    gamma = ""
    epsilon = ""
    for one in counts:
        zero = count-one
        if zero > one:
            epsilon += "1"
            gamma += "0"
        else:
            epsilon += "0"
            gamma += "1"
    epsilon = int(epsilon, 2)
    gamma = int(gamma, 2)

    print(gamma*epsilon)


if __name__ == "__main__":
    main()

