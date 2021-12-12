#!/usr/bin/env python3

import sys


def walk_graph(g, source, visited, paths):
    if source in visited:
        return

    if source.islower():
        visited.append(source)

    if source == "end":
        paths.append(visited)
        return

    for target in g[source]:
        walk_graph(g, target, visited[:], paths)

def main():
    g = {}

    for line in sys.stdin:
        source, target = line.rstrip().split("-")
        if source in g:
            g[source].append(target)
        else:
            g[source] = [target]
        if target in g:
            g[target].append(source)
        else:
            g[target] = [source]


    paths = []
    visited = []
    walk_graph(g, "start", visited, paths)

    print(len(paths))

if __name__ == "__main__":
    main()

