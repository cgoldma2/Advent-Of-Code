#!/usr/bin/env python3

import sys


def main():
    depth = 0
    pos = 0
    aim = 0

    for line in sys.stdin:
        command = line.split()
        if command[0] == "forward":
            pos += int(command[1])
            depth += aim*int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])

    print(depth*pos)

if __name__ == "__main__":
    main()

