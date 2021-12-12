#!/usr/bin/env python3

import sys


def main():
    p1 = []
    p2 = []

    while line := sys.stdin.readline():
        line = sys.stdin.readline()
        while line.rstrip() != "Player 2:":
            if line.rstrip(): p1.append(int(line))
            line = sys.stdin.readline()
        while line := sys.stdin.readline():
            p2.append(int(line))

    while p1 and p2:
        card1 = p1.pop(0)
        card2 = p2.pop(0)

        if card1 > card2:
            p1.append(card1)
            p1.append(card2)
        else:
            p2.append(card2)
            p2.append(card1)

    score = 0
    for i, card in enumerate(reversed(p1)):
        score += (i+1)*card
    for i, card in enumerate(reversed(p2)):
        score += (i+1)*card

    print(score)

if __name__ == "__main__":
    main()

