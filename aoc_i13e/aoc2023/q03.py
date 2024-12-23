import re
from itertools import product
from math import prod

from aocd import data


def part_1(s: str) -> int:
    g = s.splitlines()
    G = range(len(g))
    graph = {(r, c): [] for r, c in product(G, G) if g[r][c] in "#$%&*+-/=@"}
    for r in G:
        for match in re.finditer(r"\d+", g[r]):
            adj = {
                (r, c)
                for r in range(r - 1, r + 2)
                for c in range(match.start() - 1, match.end() + 1)
            }
            for point in adj & graph.keys():
                graph[point].append(int(match.group()))

    return sum(sum(spam) for spam in graph.values())


def part_2(s: str) -> int:
    g = s.splitlines()
    G = range(len(g))
    graph = {(r, c): [] for r, c in product(G, G) if g[r][c] in "#$%&*+-/=@"}
    for r in G:
        for match in re.finditer(r"\d+", g[r]):
            adj = {
                (r, c)
                for r in range(r - 1, r + 2)
                for c in range(match.start() - 1, match.end() + 1)
            }
            for point in adj & graph.keys():
                graph[point].append(int(match.group()))

    return sum(prod(point) for point in graph.values() if len(point) == 2)


def main() -> int:
    print(part_1(str(data)))
    print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
