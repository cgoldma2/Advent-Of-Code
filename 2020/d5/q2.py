#!/usr/bin/env python3

import sys


def main():
    seats = set()
    for seat in sys.stdin:
        row = range(128)
        col = range(8)

        for c in seat:
            if c == "B":
                row = row[len(row)//2:len(row)]
            elif c == "F":
                row = row[0:len(row)//2]
            elif c == "R":
                col = col[len(col)//2:len(col)]
            elif c == "L":
                col = col[0:len(col)//2]

        seats.add(row[0]*8+col[0])

    seats_l = sorted(list(seats))
    all_seats = set(range(seats_l[1],seats_l[-1]))

    print(all_seats.difference(seats))

if __name__ == "__main__":
    main()

