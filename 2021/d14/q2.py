#!/usr/bin/env python3

import sys
from collections import defaultdict


STEPS = 40

def main():
    old = sys.stdin.readline().rstrip()
    sys.stdin.readline()

    rules = {}
    for line in sys.stdin:
        rule = line.rstrip().split(" -> ")
        rules[rule[0]] = rule[1]
    counts = defaultdict(int)
    for i in range(len(old)-1):
        pair = old[i:i+2]
        counts[pair] += 1

    for _ in range(STEPS):
        new_counts = defaultdict(int)
        for pair, count in counts.items():
            c = rules[pair]
            p1 = pair[0] + c
            p2 = c + pair[1]

            new_counts[p1] += count
            new_counts[p2] += count
        counts = new_counts

    letter_counts = defaultdict(int)
    for pair, count in counts.items():
        letter_counts[pair[0]] += count
        letter_counts[pair[1]] += count

    print((max(letter_counts.values())-min(letter_counts.values()))/2-1)

if __name__ == "__main__":
    main()

