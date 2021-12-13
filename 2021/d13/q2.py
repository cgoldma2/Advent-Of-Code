#!/usr/bin/env python3

import sys
from matplotlib import pyplot as plt


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
        if len(instruction) < 10:
            break
        fold_paper(instruction, coords)
        print(len(set(map(tuple,coords))))

    print(coords)
    x = [c[0] for c in coords]
    y = [c[1] for c in coords]
    plt.scatter(x,y)
    plt.show()

if __name__ == "__main__":
    main()

