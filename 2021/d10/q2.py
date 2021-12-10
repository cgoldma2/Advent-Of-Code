#!/usr/bin/env python3

import sys


def main():
    closes = {')':'(', ']':'[', '}':'{', '>':'<'}
    open_vals = {val:key for key,val in closes.items()}
    values = {')':1, ']':2, '}':3, '>':4}
    scores = []
    for line in sys.stdin:
        opens = []
        incomplete = True
        for c in line:
            if c in closes.values():
                opens.append(c)
            elif c in closes:
                o = opens.pop()
                if o != closes[c]:
                    incomplete = False
                    break
        if incomplete:
            score = 0
            opens = list(reversed(opens))
            for o in opens:
                score *= 5
                score += values[open_vals[o]]
            scores.append(score)

    print(sorted(scores)[len(scores)//2])

if __name__ == "__main__":
    main()

