#!/usr/bin/env python3

import sys


def simulate_trajectory(x1, x2, y1, y2, vx, vy):
    x = 0
    y = 0

    max_y = y

    while x <= x2 and y >= y1:
        x += vx
        y += vy

        max_y = max(max_y, y)

        vy -= 1
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            return True

    return False

def main():
    line = sys.stdin.readline()
    line = line[line.index('x'):]
    x1, x2 = map(int, line[2:line.index(',')].split('..'))
    line = line[line.index('y'):]
    y1, y2 = map(int, line[2:].split('..'))

    vel_count = 0

    for vx in range(1,x2+1):
        for vy in range(y1, -1*y1+1):
            vel_count += simulate_trajectory(x1, x2, y1, y2, vx, vy)

    print(vel_count)



if __name__ == "__main__":
    main()

