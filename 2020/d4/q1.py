#!/usr/bin/env python3

import sys


def main():
    passports = [{}]
    while line := sys.stdin.readline():
        line = line.rstrip()
        if line:
            line = line.split()
            for entry in line:
                entry = entry.split(":")
                if entry[0] != "cid":
                    passports[-1][entry[0]] = entry[1]
        else:
            passports.append({})
    print(sum([len(e) == 7 for e in passports]))
if __name__ == "__main__":
    main()

