#!/usr/bin/env python3

import sys


def main():
    nums = {'abcefg': '0',
            'cf': '1',
            'acdeg': '2',
            'acdfg':'3',
            'bcdf': '4',
            'abdfg': '5',
            'abdefg': '6',
            'acf': '7',
            'abcdefg': '8',
            'abcdfg': '9'}
    unique_counts = {6: 'b',
                     8: 'c',
                     4: 'e',
                     9: 'f'}

    s = 0
    while line := sys.stdin.readline():
        pattern, output = line.split('|')
        pattern = pattern.split()
        output = output.split()

        mappings = {}

        # Sort pattern by length
        pattern.sort(key=len)

        mappings = {}
        one = pattern[0]
        seven = pattern[1]
        four = pattern[2]
        mappings[list(set(c for c in seven)-set(c for c in one))[0]] = 'a'

        counts = {chr(i): 0 for i in range(ord('a'),ord('g')+1)}
        for num in pattern:
            for letter in num:
                counts[letter] += 1
        for key, val in counts.items():
            if val in unique_counts and key not in mappings:
                mappings[key] = unique_counts[val]
            elif val == 7:
                if key in four:
                    mappings[key] = 'd'
                else:
                    mappings[key] = 'g'

        n = ''
        for num in output:
            new_num = []
            for letter in num:
                new_num.append(mappings[letter])
            new_num = ''.join(sorted(new_num))
            n += nums[new_num]
        s += int(n)
    print(s)


if __name__ == "__main__":
    main()

