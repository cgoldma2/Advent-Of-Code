#!/usr/bin/env python3

import sys


def read_danger():
    grid = []
    for line in sys.stdin:
        grid.append(list(map(int, list(line.rstrip()))))
    return grid

def inc(n, i=1):
    for _ in range(i):
        if n >= 9:
            n = 1
        else:
            n += 1
    return n

def multiply_danger(danger):
    new_danger = [row[:] for row in danger]

    # horizontally
    for i, row in enumerate(danger):
        for j in range(4):
            new_danger[i] += list(map(inc,row,[j+1]*len(row)))

    # Vertically
    danger = new_danger[:]
    for i in range(4):
        for row in danger:
            new_danger.append(list(map(inc,row,[i+1]*len(row))))

    danger = [row[:] for row in new_danger]
    rows = len(danger)
    cols = len(danger[0])

    new_danger = [[float("inf")]*(cols+2)]
    for row in danger:
        new_danger.append([float("inf")] + row + [float("inf")])
    new_danger.append([float("inf")]*(cols+2))

    return new_danger

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
    extended_danger = multiply_danger(danger)
    find_path(extended_danger)

if __name__ == "__main__":
    main()

