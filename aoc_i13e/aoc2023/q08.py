from itertools import cycle
from math import lcm

from aocd import data


def part_1(s: str) -> int:
    directions, network = s.split("\n\n")
    graph = {}
    for line in network.splitlines():
        src, dst = line.split(" = ")
        graph[src] = dst.strip("()").split(", ")

    cur = "AAA"
    for i, c in enumerate(cycle(directions), 1):
        cur = graph[cur][0] if c == "L" else graph[cur][1]
        if cur == "ZZZ":
            return i
    return 0


def part_2(s: str) -> int:
    directions, network = s.split("\n\n")
    graph = {}
    for line in network.splitlines():
        src, dst = line.split(" = ")
        graph[src] = dst.strip("()").split(", ")

    def period(cur: str) -> int:
        for i, c in enumerate(cycle(directions), 1):
            cur = graph[cur][0] if c == "L" else graph[cur][1]
            if cur.endswith("Z"):
                return i
        return 0

    return lcm(*(period(k) for k in graph if k.endswith("A")))


def main() -> int:
    print(part_1(str(data)))
    print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
