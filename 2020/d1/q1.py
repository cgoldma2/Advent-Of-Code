#!/usr/bin/env python3

import sys


def main():
    nums = [int(n) for n in sys.stdin]
    nums.sort()

    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums[i+1:]):
            s = n1 + n2
            if s == 2020:
                print(n1*n2)
                break
            elif s > 2020:
                break

if __name__ == "__main__":
	main()

