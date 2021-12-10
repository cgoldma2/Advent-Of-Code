#!/usr/bin/env python3

import sys


def main():
    closes = {')':'(', ']':'[', '}':'{', '>':'<'}
    values = {')':3, ']':57, '}':1197, '>':25137}
    points = 0
    for line in sys.stdin:
        opens = []
        for c in line:
            if c in closes.values():
                opens.append(c)
            elif c in closes:
                o = opens.pop()
                if o != closes[c]:
                    points += values[c]
                    break
    print(points)


if __name__ == "__main__":
    main()

