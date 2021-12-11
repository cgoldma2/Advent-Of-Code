#!/usr/bin/env python3

import sys
import re


def main():
    regex  = {'byr': '19[2-9][0-9]|200[0-2]',
              'iyr': '201[0-9]|2020',
              'eyr': '202[0-9]|2030',
              'hgt': '1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in',
              'hcl': '#[0-9a-f]{6}',
              'ecl': 'amb|blu|brn|gry|grn|hzl|oth',
              'pid': '[0-9]{9}'}

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

    valids = len(passports)
    for passport in passports:
        if len(passport) == 7:
            for entry, value in passport.items():
                if not re.match(regex[entry], value):
                    valids -= 1
                    break
        else:
            valids -= 1

    print(valids)

if __name__ == "__main__":
    main()

