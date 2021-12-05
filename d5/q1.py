#!/usr/bin/env python3

import sys


SIZE = 1000

def count_overlaps(vents):
    overlaps = 0
    for val in vents.values():
        if val > 1:
            overlaps += 1
    return overlaps

def main():
    vents = {(x,y): 0 for x in range(SIZE) for y in range(SIZE)}
    for line in sys.stdin:
        coords = line.split(" -> ")
        x1, y1 = map(int, coords[0].split(","))
        x2, y2 = map(int, coords[1].split(","))

        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    vents[(x,y)] += 1

    print(count_overlaps(vents))


if __name__ == "__main__":
	main()

