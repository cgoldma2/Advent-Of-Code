#!/usr/bin/env python3

import sys

def process_flashes(energy, flashes):
    flash_count = 0
    flashed = []

    while flashes:
        ox,oy = flashes.pop()
        if (ox,oy) in flashed:
            continue
        flashed.append((ox,oy))
        flash_count += 1
        energy[oy][ox] = 0
        for x in range(ox-1,ox+2):
            for y in range(oy-1,oy+2):
                if x >= 0 and x < len(energy[0]) and y >= 0 and y < len(energy) and (y != oy or x != ox):
                    if (x,y) not in flashed:
                        energy[y][x] += 1
                    if energy[y][x] > 9:
                        flashes.append((x,y))

    return flash_count

def main():
    energy = [[int(n) for n in line.rstrip()] for line in sys.stdin]

    flash_count = 0
    for line in energy:
        print(line)
    print()

    step = 1
    while True:
        flashes = []
        for y, row in enumerate(energy):
            for x, e in enumerate(row):
                if e == 9:
                    flashes.append((x,y))
                energy[y][x] += 1
        if len(flashes) == len(energy)*len(energy[0]):
            print(step-energy[0][0])
            break
        process_flashes(energy, flashes)
        step += 1

if __name__ == "__main__":
    main()

