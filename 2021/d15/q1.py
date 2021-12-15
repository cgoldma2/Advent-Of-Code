#!/usr/bin/env python3

import sys


def read_danger():
    grid = []
    for line in sys.stdin:
        grid.append(list(map(int, list(line.rstrip()))))

    rows = len(grid)
    cols = len(grid[0])

    danger = [[float("inf")]*(cols+2)]
    for i in range(rows):
        danger.append([float("inf")] + grid[i] + [float("inf")])
    danger.append([float("inf")]*(cols+2))
    return danger

def find_path(danger):
    rows = len(danger)
    cols = len(danger[0])

    table = [[float("inf") for _ in range(cols)] for _ in range(rows)]

    for row in range(1, rows):
        for col in range(1, cols):
            if row == 1 and col == 1:
                table[row][col] = 0
            else:
                table[row][col] = min(table[row][col-1],
                                      table[row-1][col]) + danger[row][col]
    print(table[rows-2][cols-2])

def main():
    danger = read_danger()
    n = find_path(danger)

if __name__ == "__main__":
    main()

