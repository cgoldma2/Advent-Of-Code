#!/usr/bin/env python3

import sys


def find_trees(m, dx, dy):
    x = 0
    y = 0
    max_x = len(m[0])
    trees = 0

    while y < len(m):
        trees += m[y][x] == "#"
        x += dx
        if x >= max_x:
            x %= max_x
        y += dy

    return trees


def main():
    m = [l.rstrip() for l in sys.stdin]
    trees = 1

    print(find_trees(m, 3, 1))
    for dx in range(1,9,2):
        trees *= find_trees(m, dx, 1)
    trees *= find_trees(m, 1, 2)

    print(trees)

if __name__ == "__main__":
    main()

