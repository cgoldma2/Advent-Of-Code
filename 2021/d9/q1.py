#!/usr/bin/env python3

import sys


def main():
    heightmap = []
    for line in sys.stdin:
        heightmap.append([int(i) for i in line.rstrip()])

    x_max = len(heightmap[0])-1
    y_max = len(heightmap)-1
    danger = 0
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            h = heightmap[y][x]
            if y > 0 and heightmap[y-1][x] <= h:
                continue
            elif y < y_max and heightmap[y+1][x] <= h:
                continue
            elif x > 0 and heightmap[y][x-1] <= h:
                continue
            elif x < x_max and heightmap[y][x+1] <= h:
                continue

            # If we pass all those checks
            danger += h+1

    print(danger)


if __name__ == "__main__":
    main()

