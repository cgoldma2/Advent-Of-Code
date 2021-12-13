#!/usr/bin/env python3

import sys


def fold_paper(instruction, coords):
    axis = instruction[11]
    idx = int(axis == 'y')
    pos = int(instruction[13:])
    print(axis, idx, pos)
    for i, coord in enumerate(coords):
        if coord[idx] > pos:
            dif = coord[idx] - pos
            coords[i][idx] = pos - dif

def main():
    coords = []
    while coord := sys.stdin.readline().strip():
        coords.append(list(map(int,coord.split(","))))

    while instruction := sys.stdin.readline().strip():
        fold_paper(instruction, coords)
        print(len(set(map(tuple,coords))))


if __name__ == "__main__":
    main()

