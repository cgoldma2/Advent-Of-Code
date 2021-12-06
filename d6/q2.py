#!/usr/bin/env python3

import sys


def main():
    init_fish = list(map(int, sys.stdin.readline().split(',')))
    days = {i: 0 for i in range(9)}
    for fish in init_fish:
        days[fish] += 1

    for _ in range(256):
        new_days = {}
        for i in range(1,9):
            new_days[i-1] = days[i]
        new_days[8] = days[0]
        new_days[6] += days[0]
        print(days)
        days = new_days

    print(sum(days.values()))

if __name__ == "__main__":
	main()

