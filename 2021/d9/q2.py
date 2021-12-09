#!/usr/bin/env python3

import sys


def find_basin(heightmap, coords, x_max, y_max, visited):
    if coords in visited:
        return
    x,y = list(coords)
    h = heightmap[y][x]

    visited.add(coords)
    if y > 0 and heightmap[y-1][x] >= h and heightmap[y-1][x] < 9:
        find_basin(heightmap, (x,y-1), x_max, y_max, visited)
    if y < y_max and heightmap[y+1][x] >= h and heightmap[y+1][x] < 9:
        find_basin(heightmap, (x,y+1), x_max, y_max, visited)
    if x > 0 and heightmap[y][x-1] >= h and heightmap[y][x-1] < 9:
        find_basin(heightmap, (x-1,y), x_max, y_max, visited)
    if x < x_max and heightmap[y][x+1] >= h and heightmap[y][x+1] < 9:
        find_basin(heightmap, (x+1,y), x_max, y_max, visited)

def main():
    heightmap = []
    for line in sys.stdin:
        heightmap.append([int(i) for i in line.rstrip()])

    x_max = len(heightmap[0])-1
    y_max = len(heightmap)-1
    basin_sizes = []
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
            visited = set()
            find_basin(heightmap, (x,y), x_max, y_max, visited)
            basin_sizes.append(len(visited))

    total = 1
    for n in sorted(basin_sizes, reverse=True)[0:3]:
        total *= n
    print(total)

if __name__ == "__main__":
    main()

