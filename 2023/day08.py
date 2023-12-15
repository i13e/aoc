from __future__ import annotations

from itertools import cycle
from math import lcm

from aocd import data
import pytest

import support


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


EXAMPLE_1 = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
EXPECTED_1 = 6

EXAMPLE_2 = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""
EXPECTED_2 = 6


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (EXAMPLE_1, EXPECTED_1, None),
        (EXAMPLE_2, None, EXPECTED_2),
        (str(data), 24253, 12357789728873),
    ),
)
def test(input_s: str, expected_1: int, expected_2: int) -> None:
    if expected_1 and (result_1 := part_1(input_s)):
        assert result_1 == expected_1

    if expected_2 and (result_2 := part_2(input_s)):
        assert result_2 == expected_2


def main() -> int:
    with support.timing():
        print(part_1(str(data)))

    with support.timing():
        print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
