#!/usr/bin/env python3

import sys


def count_nums(lines, ox, idx):
    count = 1
    counts = [int(i) for i in lines[0]]
    for line in lines[1:]:
        for i, num in enumerate(line.strip()):
            counts[i] += int(num)
        count += 1

    one = counts[idx]
    zero = count-one
    new_lines = []
    if ox:
        if one >= zero:
            for line in lines:
                if line[idx] == "1":
                    new_lines.append(line)
        else:
            for line in lines:
                if line[idx] == "0":
                    new_lines.append(line)
    else:
        if one >= zero:
            for line in lines:
                if line[idx] == "0":
                    new_lines.append(line)
        else:
            for line in lines:
                if line[idx] == "1":
                    new_lines.append(line)
    return new_lines


def main():
    lines_ox = []
    lines_co2 = []
    for line in sys.stdin:
        lines_ox.append(line.strip())
        lines_co2.append(line.strip())

    idx = 0
    while len(lines_ox) > 1:
        lines_ox = count_nums(lines_ox, True, idx)
        idx += 1

    idx = 0
    while len(lines_co2) > 1:
        lines_co2 = count_nums(lines_co2, False, idx)
        idx += 1

    line_ox = lines_ox[0]
    line_co2 = lines_co2[0]
    print(line_ox)
    print(line_co2)
    print(int(line_co2,2)*int(line_ox,2))

if __name__ == "__main__":
    main()

