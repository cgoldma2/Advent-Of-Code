#!/usr/bin/env python3

import sys


def main():
    # Set initial previous values to infinity
    # In a queue-like data structure
    prev_3 = [float("inf")]*3
    increase_count = 0
    for num in sys.stdin:
        curr = int(num)

        # Get sum of last 3
        prev_sum = sum(prev_3)

        # Cycle out last value, cycle in curr
        prev_3.pop(0)
        prev_3.append(curr)
        curr_sum = sum(prev_3)

        if curr_sum > prev_sum:
            increase_count += 1

    print(increase_count)


if __name__ == "__main__":
    main()

