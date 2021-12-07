#!/usr/bin/env python3

import sys


def main():
    fish = list(map(int, sys.stdin.readline().split(',')))

    for _ in range(80):
        print(fish)
        l = len(fish)
        for i in range(l):
            fish[i] -= 1
            if fish[i] < 0:
                fish.append(8)
                fish[i] = 6
    print(len(fish))

if __name__ == "__main__":
	main()

