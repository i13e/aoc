from __future__ import annotations

from collections import Counter

from aocd import data
import pytest

import support


def process_row(s: str) -> set[int]:
    _, win, hand = s.replace(":", "|").split("|")
    win = set(map(int, filter(str.isdigit, win.split(" "))))
    hand = set(map(int, filter(str.isdigit, hand.split(" "))))
    return win & hand


def part_1(s: str) -> int:
    return sum(
        2 ** (len(row) - 1)
        for row in map(lambda x: process_row(x), s.splitlines())
        if row
    )


def part_2(s: str) -> int:
    graph = Counter()
    lines = s.splitlines()
    for i, row in enumerate(map(lambda x: process_row(x), s.splitlines())):
        for j in range(i + 1, min(len(lines), i + 1 + len(row))):
            graph[j] += graph[i] + 1
    return sum(graph.values()) + len(lines)


INPUT_S = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
EXPECTED_1 = 13
EXPECTED_2 = 30


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (INPUT_S, EXPECTED_1, EXPECTED_2),
        (str(data), 23941, 5571760),
    ),
)
def test_d(input_s: str, expected_1: int, expected_2: int) -> None:
    if result_1 := part_1(input_s):
        assert result_1 == expected_1

    if result_2 := part_2(input_s):
        assert result_2 == expected_2


def main() -> int:
    with support.timing():
        print(part_1(str(data)))

    with support.timing():
        print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
