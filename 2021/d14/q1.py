#!/usr/bin/env python3

import sys


STEPS = 10

def main():
    old = sys.stdin.readline().rstrip()
    sys.stdin.readline()

    rules = {}
    for line in sys.stdin:
        rule = line.rstrip().split(" -> ")
        rules[rule[0]] = rule[1]

    print(old)
    new = ""
    for _ in range(STEPS):
        new = old[0]
        for i in range(len(old)-1):
            pair = old[i] + old[i+1]
            new += rules[pair] + old[i+1]
        old = new

    counts = {}
    for c in old:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    print(max(counts.values())-min(counts.values()))

if __name__ == "__main__":
    main()

