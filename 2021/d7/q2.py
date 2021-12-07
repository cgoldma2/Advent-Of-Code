#!/usr/bin/env python3

import sys


def main():
    crabs = list(map(int, sys.stdin.readline().split(',')))

    min_spend = float('inf')
    for crab in crabs:
        spend = 0
        for crab2 in crabs:
            dx = abs(crab2-crab)
            for n in range(1,dx+1):
                spend += n
        min_spend = min(spend, min_spend)
    print(min_spend)

if __name__ == "__main__":
	main()

