#!/usr/bin/env python3

import sys


def main():
    crabs = list(map(int, sys.stdin.readline().split(',')))

    min_spend = float('inf')
    for crab in crabs:
        spend = 0
        for crab2 in crabs:
            spend += abs(crab2-crab)
        min_spend = min(spend, min_spend)
    print(min_spend)

if __name__ == "__main__":
	main()

