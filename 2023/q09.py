from __future__ import annotations

from itertools import pairwise

from aocd import data
import pytest

import support


def simplify(nums: list[int]) -> list[list[int]]:
    res = [nums]
    while any(e for e in res[-1]):
        res.append([b - a for a, b in pairwise(res[-1])])
    return res


def extrapolate(layers: list[list[int]]) -> int:
    for a, b in pairwise(layers[::-1]):
        b.append(a[-1] + b[-1])
    return layers[0][-1]


def part_1(s: str) -> int:
    histories = [list(map(int, line.split())) for line in s.splitlines()]
    return sum(extrapolate(simplify(h)) for h in histories)


def part_2(s: str) -> int:
    histories = [list(map(int, line.split())) for line in s.splitlines()]
    return sum(extrapolate(simplify(h[::-1])) for h in histories)


INPUT_S = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""
EXPECTED_1 = 114
EXPECTED_2 = 2


@pytest.mark.parametrize(
    ("input_s", "expected_1", "expected_2"),
    (
        (INPUT_S, EXPECTED_1, EXPECTED_2),
        (str(data), 1725987467, 971),
    ),
)
def test(input_s: str, expected_1: int, expected_2: int) -> None:
    if expected_1:
        assert part_1(input_s) == expected_1

    if expected_2:
        assert part_2(input_s) == expected_2


def main() -> int:
    with support.timing():
        print(part_1(str(data)))

    with support.timing():
        print(part_2(str(data)))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
